from json import load
from pathlib import Path

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from buttons import CONTACT_ME_BTN
from fsm import DialogStates
from handlers import dialog_handler

faq_states = {
    'faq_why_tg': DialogStates.faq_why_tg,
    'faq_development': DialogStates.faq_development,
    'faq_usage': DialogStates.faq_usage,
    'faq_taboo': DialogStates.faq_taboo,
    'faq_cost': DialogStates.faq_cost,
    'faq_cost_calc': DialogStates.faq_cost_calc,
    'faq_llc': DialogStates.faq_llc,
    'faq_warranty': DialogStates.faq_warranty,
    'faq_change': DialogStates.faq_change,
    'faq_bot_location': DialogStates.faq_bot_location
}


def generate_n():
    """
    Generator function that increments the value of n every 5 cycles.

    :return: Yields the current value of n on each iteration.
    """
    n = 1
    cycle = 0

    while True:
        yield n
        cycle += 1
        if cycle % 5 == 0:
            n += 1


def get_faq_answers():
    file_path = Path(__file__).resolve().parent / 'FAQ.json'
    with open(file_path, "r", encoding="utf-8") as file:
        faq_data = load(file)
    windows = []
    n_generator = generate_n()

    for key in faq_data.keys():
        state = faq_states[key]
        text = '\n\n'.join(faq_data[key])
        n = next(n_generator)

        windows.append(
            Window(
                Const(text),
                CONTACT_ME_BTN,
                Button(
                    Const('Назад'),
                    id=f'faq_{n}',
                    on_click=dialog_handler
                ),
                state=state,
            )
        )

    return windows


faq_windows = get_faq_answers()
