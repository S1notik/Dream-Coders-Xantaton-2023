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


# Кнопки для инфографии
infography_buttons = [
        [
            InlineKeyboardButton(
                text="Батарейки",
                callback_data="battery_infography")
        ],
        [
            InlineKeyboardButton(
                text="Композитная упаковка",
                callback_data="сomposite_package_infography")
        ],
        [
            InlineKeyboardButton(
                text="Металл",
                callback_data="metal_infography")
        ],
        [
            InlineKeyboardButton(
                text="Пластик",
                callback_data="plastic_infography")
        ],
        [
            InlineKeyboardButton(
                text="Стекло",
                callback_data="glass_infography")
        ],
        [
            InlineKeyboardButton(
                text="Экологичность упаковки",
                callback_data="environmental_friendliness_of_packaging_infography")
        ]
    ]
infography_keyboard = InlineKeyboardMarkup(inline_keyboard=infography_buttons,
                                resize_keyboard=True,
                                one_time_keyboard=True,
                                input_field_placeholder="Choice a button",
                                selective=True)