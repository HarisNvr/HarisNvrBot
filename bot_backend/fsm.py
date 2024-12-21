from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

aio_storage = MemoryStorage()


class DialogStates(StatesGroup):
    """
    Defines the states for managing dialogs in an FSM context.
    """

    start = State()
    faq_1 = State()
    faq_2 = State()

    faq_why_tg = State()
    faq_development = State()
    faq_usage = State()
    faq_taboo = State()
    faq_cost = State()
    faq_cost_calc = State()
    faq_llc = State()
    faq_warranty = State()
    faq_change = State()
    faq_bot_location = State()
