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

