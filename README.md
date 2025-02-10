#  Бот-помощник програмиста HarisNvr

## Ссылка на бота: https://t.me/HarisNvrBot

## Что умеет?

**Простой бот для предоставления базовой информации и ответа на частые вопросы**

### Используемые технологии

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Aiogram](https://img.shields.io/badge/Aiogram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://pypi.org/project/aiogram/)
[![Aiogram-dialog](https://img.shields.io/badge/Aiogram--dialog-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://github.com/aiogram/aiogram-dialog)
[![Docker](https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

### Развернуть проект на удаленном сервере:

**Предполагается, что на вашей машине уже установлен Docker с плагином Docker-compose!**

Инструкция по установке: https://docs.docker.com/engine/install/

- Клонировать репозиторий и перейти в него:
```
cd HarisNvrBot
```

- Настраиваем переменные окружения:
```
sudo nano .env
```

```
# ПРИМЕР ФАЙЛА .env

#BOT
TOKEN=abcdef123456  # Telegram_API_bot_token
```

- Запустить Docker compose:
```
sudo docker compose up -d
```

## Команды, вводимые через '/' в чате:

```
start - Запуск бота
faq - Ответы на частые вопросы
```
