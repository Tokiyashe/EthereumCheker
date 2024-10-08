# EthereumCheker
Программа "Ethereum Wallet Checker" — это мощный инструмент, предназначенный для проверки и мониторинга баланса Ethereum-кошельков с использованием современного графического интерфейса. 

Основные функции:

1. Генерация мнемонических фраз**: Программа использует библиотеку Mnemonic для создания безопасных мнемоник, что позволяет легко получать адреса кошельков.

2. Проверка баланса**: С помощью API Infura и библиотеки Web3 приложение извлекает информацию о балансе сгенерированных адресов. Если баланс положительный, адрес сохраняется в текстовом файле для дальнейшего использования.

3. Обновление цены Ethereum**: Программа автоматически обновляет цену ETH каждую минуту через API CoinGecko, что позволяет пользователю видеть актуальные данные о стоимости.

4. Графический интерфейс**: На базе Tkinter, интерфейс приложения прост и интуитивно понятен. Пользователь вводит свой API-ключ, нажимает кнопку для запуска проверки и получает результаты в текстовом поле, которое удобно прокручивается.

5. Музыкальное сопровождение**: При обнаружении адреса с положительным балансом приложение меняет цвет текста на красный и воспроизводит музыкальный файл, добавляя элемент увлекательности и азартности в процесс проверки.

Как это работает:

Пользователь вводит свой API-ключ Infura, после чего запускает проверку. Программа генерирует мнемонические фразы, создает адреса, проверяет их баланс и обновляет информацию о цене ETH. Если на каком-либо из адресов обнаруживается баланс, адрес сохраняется и пользователь получает уведомление.

Заключение:

"Ethereum Wallet Checker" не только помогает пользователям отслеживать состояние своих инвестиций, но и делает процесс проверки увлекательным. Приложение сочетает в себе функциональность, удобство и немного развлечения, что делает его идеальным инструментом для любого, кто интересуется криптовалютами.
Пошаговая инструкция по запуску программы

ИНСТРУКЦИЯ ПО ИСПОЛЬЗОВАНИЮ

1. Скачайте архив с программой:
   - Получите архив, содержащий файл программы (wallet_checker.py), текстовый документ для сохранения адресов (Wallet+.txt) и папку с музыкой (Music).

2. Разархивируйте файл:
   - Разархивируйте содержимое в удобное для вас место на компьютере, например, на рабочий стол.

3. Установите Python:
   - Убедитесь, что у вас установлен Python версии 3.6 или выше. Вы можете скачать его с официального сайта Python (https://www.python.org/downloads/).

4. Установите необходимые библиотеки:
   - Откройте командную строку (cmd) или терминал и выполните следующую команду, чтобы установить все необходимые библиотеки:
     pip install mnemonic eth-account web3 requests pygame

5. Получите API-ключ Infura:
   - Перейдите на Infura (https://infura.io/).
   - Зарегистрируйтесь или войдите в свою учетную запись.
   - Создайте новый проект. После создания проекта вы получите API-ключ (Project ID). Скопируйте его, он вам понадобится для работы программы.

6. Запустите программу:
   - В командной строке или терминале перейдите в папку, где находится файл программы:
     cd путь_к_папке_с_программой
   - Выполните команду для запуска программы:
     python wallet_checker.py

7. Введите API-ключ:
   - В открывшемся окне программы введите ваш API-ключ Infura в соответствующее поле и нажмите кнопку "Запустить проверку".

8. Наблюдайте за результатами:
   - Программа начнет генерировать адреса Ethereum и проверять их балансы. Вы увидите адреса и их балансы в текстовом окне.
   - Если адрес с балансом больше нуля, текст станет красным, и будет проигрываться музыкальный файл.
