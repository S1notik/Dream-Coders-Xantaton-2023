from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



# Наши соц-сети
useful_links_buttons = [
    [
        InlineKeyboardButton(
            text="Телеграмм🕊️",
            url="https://t.me/S1notik",

        ),
        InlineKeyboardButton(
            text="Discord💬",
            url="https://discord.gg/BGVGCcnx"
        ),
    ]
]
useful_links_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=useful_links_buttons,
                                resize_keyboard=True,
                                one_time_keyboard=True,
                                input_field_placeholder="Choice a button",
                                selective=True)



# Кнопки для видов сырья
types_materials_inline_buttons = [
        [
            InlineKeyboardButton(
                text="Стеклянные бутылки и банки",
                callback_data="glass_bottles_and_jars_typematerial")
        ],
        [
            InlineKeyboardButton(
                text="Макулатура",
                callback_data="waste_paper_typematerial")
        ],
        [
            InlineKeyboardButton(
                text="Пластиковые ящики ПНД",
                callback_data="HDPE_plastic_boxes_typematerial")
        ],
        [
            InlineKeyboardButton(
                text="Батарейки",
                callback_data="batteries_typematerial")
        ],
        [
            InlineKeyboardButton(
                text="Канистры ПНД, ПВД",
                callback_data="HDPE_LDPE_canisters_typematerial")
        ],
        [
            InlineKeyboardButton(
                text="Стретч-пленка ПВД",
                callback_data="LDPE_Stretch_film_typematerial")
        ],
        [
            InlineKeyboardButton(
                text="Пленка ПВД",
                callback_data="LDPE_film_typematerial")
        ],
        [
            InlineKeyboardButton(
                text="Крышки ПНД, ПВД, ПП",
                callback_data="HDPE_LDPE_PP_covers_typematerial")
        ],
        [
            InlineKeyboardButton(
                text="Белые ПЭТ-бутылки от напитков",
                callback_data="white_PET_bottles_from_drinks_typematerial")
        ],
        [
            InlineKeyboardButton(
                text="Пакеты фасовочные и пакеты-майки ПНД, ПВД",
                callback_data="packing_packages_and_packagesTshirts_of_HDPE_LDPE_typematerial")
        ],
        [
            InlineKeyboardButton(
                text="ПЭТ-бутылки от напитков и растительного масла",
                callback_data="PET_bottles_from_beverages_and_vegetable_oil_typematerial")
        ],
        [
            InlineKeyboardButton(
                text="Алюминиевые банки",
                callback_data="aluminum_cans_typematerial")
        ]
    ]
types_materials_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=types_materials_inline_buttons)


# Кнопки для интересных фактов
link_for_post_inline_buttons = [
        [
            InlineKeyboardButton(
            text="Все новости здесь⬇️",
            url="https://vk.com/eco4u2"
        )
        ]
    ]
link_for_post_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=link_for_post_inline_buttons,
                                resize_keyboard=True,
                                one_time_keyboard=True,
                                input_field_placeholder="Choice a button",
                                selective=True)


# Кнопки для интересных фактов
interesting_facts_inline_buttons = [
        [
            InlineKeyboardButton(
                text="5 причин сортировать♻️",
                callback_data="reasons_to_sort"),
        ],
        [
            InlineKeyboardButton(
                text="Куда направляются отходы на переработку♻️",
                callback_data="where_the_waste_is_sent_for_recycling")
        ]
    ]
interesting_facts_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=interesting_facts_inline_buttons,
                                resize_keyboard=True,
                                one_time_keyboard=True,
                                input_field_placeholder="Choice a button",
                                selective=True)