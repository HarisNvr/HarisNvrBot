from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager


async def message_get_data(dialog_manager: DialogManager, **kwargs):
    """
    Retrieve data for the main window, including the user's name.

    :param dialog_manager: DialogManager instance used to manage the dialog
                           state.
    :param kwargs: Additional arguments, if any.
    :return: A dictionary containing the user's name.
    """

    event = dialog_manager.event
    if isinstance(event, CallbackQuery):
        event = event.message

    user_name = event.chat.first_name

    return {
        'name': user_name
    }
