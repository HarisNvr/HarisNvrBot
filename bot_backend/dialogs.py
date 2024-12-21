from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Format, Const

from bot_backend.buttons import (
    CONTACT_ME_BTN, FAQ_FOOTER_CLM, FAQ_CLM_1, FAQ_CLM_2
)
from bot_backend.fsm import DialogStates
from bot_backend.handlers import dialog_handler
from bot_backend.utils import message_get_data

FAQ_HEADER = Format(
    'Вы находитесь в разделе <b>Часто задаваемые вопросы (ЧаВо)</b>'
    '\n\nТут вы можете найти ответы на распространённые вопросы, которые '
    'возникают при разработке ТГ-ботов.'
    '\n\nЕсли вы не нашли ответ на свой вопрос - не стесняйтесь написать '
    'напрямую <b>Харо́</b> в личные сообщения!'
    )

star_window = Window(
    Format(
        'Здравствуйте, <b>{name}!</b>'
        '\n'
        '\nВас приветствует бот-помощник Python-разработчика '
        '<b>Харалампия Михайлова</b> aka <b>HarisNvr</b> aka <b>Харо́!</b>'
        '\n\n<u>Мои задачи:</u> ответить на часто задаваемые вопросы '
        '(<b>ЧаВо</b>) и помочь вам связаться с <b>Харо́.</b>'
    ),
    Button(
        Const(
            'Ответы на ЧаВо'
        ),
        id='faq_1',
        on_click=dialog_handler
    ),
    CONTACT_ME_BTN,
    state=DialogStates.start,
    getter=message_get_data
)

faq_window_1 = Window(
    FAQ_HEADER,
    FAQ_CLM_1,
    Button(
        Const(
            'Следующая страница \U000023ED'
        ),
        id='faq_2',
        on_click=dialog_handler
    ),
    FAQ_FOOTER_CLM,
    state=DialogStates.faq_1
)

faq_window_2 = Window(
    FAQ_HEADER,
    FAQ_CLM_2,
    Button(
        Const(
           '\U000023EE Предыдущая страница'
        ),
        id='faq_1',
        on_click=dialog_handler
    ),
    FAQ_FOOTER_CLM,
    state=DialogStates.faq_2
)
