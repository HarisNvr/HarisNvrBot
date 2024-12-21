from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot_backend.fsm import DialogStates


async def dialog_handler(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager
):
    """
    Redirect user to a certain section.

    :param callback: The CallbackQuery object triggered by the button press.
    :param button: The Button instance associated with this action.
    :param manager: DialogManager instance used to manage the dialog state.
    """

    button_pressed_id = button.widget_id

    if button_pressed_id == 'start':
        await manager.switch_to(DialogStates.start)
    elif button_pressed_id == 'faq_1':
        await manager.switch_to(DialogStates.faq_1)
    elif button_pressed_id == 'faq_2':
        await manager.switch_to(DialogStates.faq_2)

    if button_pressed_id == 'faq_why_tg':
        await manager.switch_to(DialogStates.faq_why_tg)
    elif button_pressed_id == 'faq_development':
        await manager.switch_to(DialogStates.faq_development)
    elif button_pressed_id == 'faq_usage':
        await manager.switch_to(DialogStates.faq_usage)
    elif button_pressed_id == 'faq_taboo':
        await manager.switch_to(DialogStates.faq_taboo)
    elif button_pressed_id == 'faq_cost':
        await manager.switch_to(DialogStates.faq_cost)
    elif button_pressed_id == 'faq_cost_calc':
        await manager.switch_to(DialogStates.faq_cost_calc)
    elif button_pressed_id == 'faq_llc':
        await manager.switch_to(DialogStates.faq_llc)
    elif button_pressed_id == 'faq_warranty':
        await manager.switch_to(DialogStates.faq_warranty)
    elif button_pressed_id == 'faq_change':
        await manager.switch_to(DialogStates.faq_change)
    elif button_pressed_id == 'faq_bot_location':
        await manager.switch_to(DialogStates.faq_bot_location)
