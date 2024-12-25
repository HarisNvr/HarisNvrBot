from aiogram_dialog.widgets.kbd import Url, Button, Column
from aiogram_dialog.widgets.text import Const

from handlers import dialog_handler

CONTACT_ME_BTN = Url(
    Const('Связаться \U0001F4E9'),
    Const('https://t.me/HarisNvrsk')
)

FAQ_BTN = Button(
    Const('Вернуться назад'),
    id='faq_1',
    on_click=dialog_handler
)

RETURN_TO_MENU_BTN = Button(
    Const(
        'Вернуться в меню \U000021A9'
    ),
    id='start',
    on_click=dialog_handler
)

FAQ_CLM_1 = Column(
    Button(
        Const(
            '1) Для чего нужен ТГ-бот?'
        ),
        id='faq_why_tg',
        on_click=dialog_handler
    ),
    Button(
        Const(
            '2) Как происходит разработка?'
        ),
        id='faq_development',
        on_click=dialog_handler
    ),
    Button(
        Const(
            '3) Какие возможности у ТГ-ботов?'
        ),
        id='faq_usage',
        on_click=dialog_handler
    ),
    Button(
        Const(
            '4) Какие есть ТАБУ при разработке?'
        ),
        id='faq_taboo',
        on_click=dialog_handler
    ),
    Button(
        Const(
            '5) Какая стоимость работ?'
        ),
        id='faq_cost',
        on_click=dialog_handler
    )
)

FAQ_CLM_2 = Column(
    Button(
        Const(
            '6) От чего зависит стоимость?'
        ),
        id='faq_cost_calc',
        on_click=dialog_handler
    ),
    Button(
        Const(
            '7) Кому оказываете услуги?'
        ),
        id='faq_llc',
        on_click=dialog_handler
    ),
    Button(
        Const(
            '8) Есть ли гарантия?'
        ),
        id='faq_warranty',
        on_click=dialog_handler
    ),
    Button(
        Const(
            '9) Можно ли менять бота?'
        ),
        id='faq_change',
        on_click=dialog_handler
    ),
    Button(
        Const(
            '10) Где будет находиться бот?'
        ),
        id='faq_bot_location',
        on_click=dialog_handler
    )
)
