import types

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



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


'''def get_infography_keyboard():

    # Кнопки для инфографии
    infography_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Батарейки",
                callback_data="somecallback"
            )
        ],
        [
            InlineKeyboardButton(
                text="Бумага",
                callback_data="somecallback"
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
                callback_data="somecallback"
            )
        ],
        [
            InlineKeyboardButton(
                text="Пластик",
                callback_data="somecallback"
            )
        ],
        [
            InlineKeyboardButton(
                text="Стекло",
                callback_data="somecallback"
            )
        ],
        [
            InlineKeyboardButton(
                text="Экологичность упаковки",
                callback_data="somecallback"
            )
        ],
        [
            InlineKeyboardButton(
                text="Что содержит мусорное ведро?",
                callback_data="somecallback"
            )
        ],
        [
            InlineKeyboardButton(
                text="Ответственное потребление",
                callback_data="somecallback"
            )
        ]
    ], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Choice a button", selective=True)

    keyboard = types.InlineKeyboardMarkup(types_materials_inline_keyboard)
    return keyboard'''


def get_infography_keyboard():

    # Кнопки для инфографии
    infography_keyboard = InlineKeyboardMarkup(row_width=1,
                                               resize_keyboard=True,
                                               one_time_keyboard=True,
                                               input_field_placeholder="Choice a button",
                                               selective=True)

    infography_keyboard.add(InlineKeyboardButton(text="Батарейки", url="https://www.youtube.com/"),
                            InlineKeyboardButton(text="Бумага", url="https://www.youtube.com/"))

    return infography_keyboard


'''buttons = [
        [
            types.InlineKeyboardButton(text="-1", callback_data="num_decr"),
            types.InlineKeyboardButton(text="+1", callback_data="num_incr")
        ],
        [types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")]
    ]
keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)'''



# Кнопки для инфографии
infography_builder = InlineKeyboardBuilder()
infography_builder.row(InlineKeyboardButton(
    text="Батарейки",
    callback_data="battery_infography")
)
infography_builder.row(InlineKeyboardButton(
    text="Композитная упаковка",
    callback_data="сomposite_package_infography")
)
infography_builder.row(InlineKeyboardButton(
    text="Металл",
    callback_data="metal_infography")
)
infography_builder.row(InlineKeyboardButton(
    text="Пластик",
    callback_data="plastic_infography")
)
infography_builder.row(InlineKeyboardButton(
    text="Стекло",
    callback_data="glass_infography")
)
infography_builder.row(InlineKeyboardButton(
    text="Экологичность упаковки",
    callback_data="environmental_friendliness_of_packaging_infography")
)
'''
builder.row(InlineKeyboardButton(
    text="Бумага",
    callback_data="paper_infography")
)
builder.row(InlineKeyboardButton(
    text="Что содержит мусорное ведро?",
    callback_data="what_is_contain_bin_infography")
)
builder.row(InlineKeyboardButton(
    text="Ответственное потребление",
    callback_data="responsible_consumption_infography")
)
'''