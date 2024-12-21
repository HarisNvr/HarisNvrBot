from asyncio import sleep

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, StartMode

from bot_backend.dialogs import star_window, faq_window_1, faq_window_2
from bot_backend.faq_windows import faq_windows
from bot_backend.settings import COMMANDS_FORMAT_LIST, COMMANDS_TO_STATES

main_router = Router()

main_dialog = Dialog(
    star_window,
    faq_window_1,
    faq_window_2,
    *faq_windows
)

main_router.include_router(main_dialog)


@main_router.message(Command(commands=COMMANDS_FORMAT_LIST))
async def commands_handler(message: Message, dialog_manager: DialogManager):
    """
    Handles the commands.

    :param dialog_manager: DialogManager object.
    :param message: The message sent by the user.
    :return: None
    """

    message_text = message.text.lower()

    if message_text != '/start':
        await message.delete()
        await sleep(0.5)

    state = COMMANDS_TO_STATES.get(message_text)
    if state:
        await dialog_manager.start(
            state,
            mode=StartMode.NEW_STACK
        )


@main_router.message(F)
async def misc_router(message: Message):
    """
    Handles any message that doesn't match the previous parameters.

    :param message: The message sent by the user.
    :return: None
    """

    await message.answer(
        f'Извините, {message.from_user.first_name}'
        '\n\nЯ не понимаю вас, пожалуйста выберите команду из меню или '
        'перезапустите диалог с помощью команды: /start'
    )
