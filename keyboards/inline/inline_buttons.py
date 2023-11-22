import types

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



# Кнопки для полезных ссылок
useful_links_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Как собирать отходы♻️",
            url="https://vk.com/video-211825217_456239329"
        ),
        InlineKeyboardButton(
            text="Вредный пластик♻️",
            url="https://www.youtube.com/watch?v=zQpW0OQOYLo"
        )
    ],
    [
        InlineKeyboardButton(
            text="Наш ВКонтакте👀",
            url="https://vk.com/eco4u2"
        ),
        InlineKeyboardButton(
            text="Наш Телеграмм🕊️",
            url="https://t.me/yugraecology"
        ),
        InlineKeyboardButton(
            text="Наш Одноклассники👋",
            url="https://ok.ru/group/55933980573950"
        ),
    ]
])



# Кнопки для видов сырья
types_materials_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Стеклянные бутылки и банки"
        )
    ],
    [
        InlineKeyboardButton(
            text="Макулатура"
        )
    ],
    [
        InlineKeyboardButton(
            text="Пластиковые ящики ПНД"
        )
    ],
    [
        InlineKeyboardButton(
            text="Батарейки"
        )
    ],
    [
        InlineKeyboardButton(
            text="Канистры ПНД, ПВД"
        )
    ],
    [
        InlineKeyboardButton(
            text="Стретч-пленка ПВД"
        )
    ],
    [
        InlineKeyboardButton(
            text="Пленка ПВД"
        )
    ],
    [
        InlineKeyboardButton(
            text="Крышки ПНД, ПВД, ПП"
        )
    ],
    [
        InlineKeyboardButton(
            text="Белые ПЭТ-бутылки от напитков"
        )
    ],
    [
        InlineKeyboardButton(
            text="Пакеты фасовочные и пакеты-майки ПНД, ПВД"
        )
    ],
    [
        InlineKeyboardButton(
            text="ПЭТ-бутылки от напитков и растительного масла"
        )
    ],
    [
        InlineKeyboardButton(
            text="Алюминиевые банки"
        )
    ]
])


# Кнопки для интересных фактов
interesting_facts_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="5 причин сортировать♻️"
        ),
        InlineKeyboardButton(
            text="Куда направляются отходы на переработку♻️"
        )
    ]
])


# Кнопки для инфографии
STEP1_EXTEND_CB = "extend"
STEP1_COLLAPSE_CB = "collapse"
STEP1_SETTINGS_CB = "settings"

keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Батарейки",
                             callback_data=STEP1_EXTEND_CB)],
    [
        InlineKeyboardButton(text="Композитная упаковка", callback_data=STEP1_COLLAPSE_CB)],
    [
        InlineKeyboardButton(text="Металл", callback_data=STEP1_COLLAPSE_CB)],
    [
        InlineKeyboardButton(text="Пластик", callback_data=STEP1_COLLAPSE_CB)],
    [
        InlineKeyboardButton(text="Стекло", callback_data=STEP1_COLLAPSE_CB)],
    [
        InlineKeyboardButton(text="Экологичность упаковки", callback_data=STEP1_COLLAPSE_CB)],
    [
        InlineKeyboardButton(text="Что содержит мусорное ведро?", callback_data=STEP1_COLLAPSE_CB)],
    [
        InlineKeyboardButton(text="Ответственное потребление", callback_data=STEP1_COLLAPSE_CB)],
]
)

infography_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Батарейки",
            callback_data="bat",
        )
    ],
    [
        InlineKeyboardButton(
            text="Бумага",
            callback_data="paper"
        )
    ],
    [
        InlineKeyboardButton(
            text="Композитная упаковка",
            callback_data="somecallback"
        )
    ],
    [
        InlineKeyboardButton(
            text="Металл",
            callback_data="mettal"
        )
    ],
    [
        InlineKeyboardButton(
            text="Пластик",
            callback_data="plast"
        )
    ],
    [
        InlineKeyboardButton(
            text="Стекло",
            callback_data="botter"
        )
    ],
    [
        InlineKeyboardButton(
            text="Экологичность упаковки",
            callback_data="a"
        )
    ],
    [
        InlineKeyboardButton(
            text="Что содержит мусорное ведро?",
            callback_data="b"
        )
    ],
    [
        InlineKeyboardButton(
            text="Ответственное потребление",
            callback_data="v")
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Choice a button", selective=True)

