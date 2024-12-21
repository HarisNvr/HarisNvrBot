from os import getenv

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.types import BotCommand
from dotenv import load_dotenv

from bot_backend.fsm import DialogStates

load_dotenv()

TOKEN = getenv('TOKEN')
BOT = Bot(TOKEN, default=DefaultBotProperties(parse_mode='HTML'))

COMMANDS = [
    BotCommand(
        command='start',
        description='Запуск бота'
    ),
    BotCommand(
        command='faq',
        description='Ответы на ЧаВо'
    )
]

COMMANDS_TO_STATES = {
    '/start': DialogStates.start,
    '/faq': DialogStates.faq_1
}

COMMANDS_FORMAT_LIST = [
    command.lstrip('/') for command in COMMANDS_TO_STATES.keys()
]
