# Проект telegram_test

telegram_test - это тестовый бот для Telegram, который присылает картинки котиков и 
играет с вами у кого больше загаданное число.

## Установка

1. Клонируйте репозиторий с github
2. Создайте виртуальное окружение
3. Установите зависимости `pip install -r requirements.txt`
4. Создайте файл `settings.py`
5. Впишите в settings.py переменные:
```
API_KEY = "API-ключ бота"
USER_EMOJI = [":smirk:", ":blush:", ":smile:", ":hand:"]
```
6. Запустите бота командой `python main.py`