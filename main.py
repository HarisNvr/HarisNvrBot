from asyncio import run

from aiogram import Dispatcher
from aiogram_dialog import setup_dialogs

from bot_backend.fsm import aio_storage
from bot_backend.router import main_router
from bot_backend.settings import BOT, COMMANDS


async def bot_main():
    """
    Main bot logic function. Contains: Dispatcher object, all the routers and
    infinity polling instruction.

    :return: None
    """

    dp = Dispatcher(storage=aio_storage)
    dp.include_router(main_router)
    setup_dialogs(dp)

    await BOT.set_my_commands(COMMANDS)
    await dp.start_polling(BOT)


if __name__ == '__main__':
    run(bot_main())
