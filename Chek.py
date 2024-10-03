import time
import threading
import requests
from mnemonic import Mnemonic
from eth_account import Account
from web3 import Web3
import tkinter as tk
from tkinter import scrolledtext
import pygame
import os

# Включаем функции HD-кошелька
Account.enable_unaudited_hdwallet_features()

class WalletCheckerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Ethereum Wallet Checker")
        self.master.config(bg="black")  # Фон окна

        self.total_balance_usd = 0.0
        self.usd_price = 2000  # Начальная цена ETH
        self.infura_api_key = ""  # API-ключ Infura

        # Инициализация pygame для воспроизведения музыки
        pygame.mixer.init()

        # Верхняя панель
        self.header_frame = tk.Frame(master, bg="black")
        self.header_frame.pack(fill=tk.X)

        self.title_label = tk.Label(self.header_frame, text="Ethereum Wallet Checker", fg="green", bg="black", font=("Helvetica", 16))
        self.title_label.pack(side=tk.LEFT, padx=10)

        # Поле ввода API-ключа Infura
        self.api_frame = tk.Frame(master, bg="black")
        self.api_frame.pack(pady=10)

        self.api_label = tk.Label(self.api_frame, text="API-ключ Infura:", fg="green", bg="black")
        self.api_label.pack(side=tk.LEFT)

        self.api_entry = tk.Entry(self.api_frame, width=40, bg="black", fg="green", insertbackground='green')
        self.api_entry.pack(side=tk.LEFT)

        self.start_button = tk.Button(master, text="Запустить проверку", command=self.start_checking, bg="black", fg="green")
        self.start_button.pack(pady=10)

        self.log_area = scrolledtext.ScrolledText(master, width=50, height=20, bg="black", fg="green", insertbackground='green')
        self.log_area.pack(pady=10)

        self.is_running = False
        self.file_path = "Wallet+.txt"  # Укажите путь к файлу для сохранения адресов

    def fetch_eth_price(self):
        while self.is_running:
            try:
                response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd")
                data = response.json()
                self.usd_price = data["ethereum"]["usd"]
                self.log(f"Актуальная цена ETH: ${self.usd_price:.2f}")
            except Exception as e:
                self.log(f"Ошибка получения цены: {e}")

            time.sleep(60)  # Обновление цены каждую минуту

    def generate_mnemonic(self):
        mnemo = Mnemonic("english")
        return mnemo.generate(strength=128)

    def get_address_from_mnemonic(self, mnemonic_phrase):
        acct = Account.from_mnemonic(mnemonic_phrase)
        return acct.address

    def check_balance(self, address):
        # Получаем API-ключ из поля ввода
        self.infura_api_key = self.api_entry.get()
        w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{self.infura_api_key}'))
        balance = w3.eth.get_balance(address)
        return w3.from_wei(balance, 'ether')

    def save_address_if_balance(self, address, balance):
        if balance > 0:
            with open(self.file_path, 'a') as file:
                file.write(f"{address}\n")
            self.total_balance_usd += balance * self.usd_price
            self.log(f"Адрес с балансом сохранен: {address}")
            self.highlight_balance()  # Зажигаем текст и проигрываем музыку

    def highlight_balance(self):
        # Изменяем цвет текста на красный и проигрываем музыку
        self.log_area.config(fg="red")
        music_file = os.path.join("Music", "123.mp3")  # Укажите имя вашего музыкального файла
        if os.path.exists(music_file):
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play()

    def log(self, message):
        self.log_area.insert(tk.END, message + '\n')
        self.log_area.yview(tk.END)  # Прокручиваем вниз

    def balance_checker(self):
        while self.is_running:
            mnemonic_phrase = self.generate_mnemonic()
            address = self.get_address_from_mnemonic(mnemonic_phrase)
            balance = self.check_balance(address)

            self.log(f"Адрес Ethereum: {address}")
            self.log(f"Баланс: {balance} ETH")

            self.save_address_if_balance(address, balance)

            time.sleep(1)

    def start_checking(self):
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.log_area.delete(1.0, tk.END)  # Очищаем текстовое поле

        self.balance_thread = threading.Thread(target=self.balance_checker)
        self.balance_thread.start()

        self.price_thread = threading.Thread(target=self.fetch_eth_price)
        self.price_thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = WalletCheckerApp(root)
    root.mainloop()
