from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

# Кнопки для главного меню
start_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        # KeyboardButton(
        #     text="Пункты сбора♻️"
        # ),
        KeyboardButton(
            text="Правила приёма📃"
        ),
        KeyboardButton(
            text="Виды сырья🗑️"
        )
    ],
    [
        KeyboardButton(
            text="Забрать опыт✨️"
        ),
        KeyboardButton(
            text="Профиль👤"
        ),
        KeyboardButton(
            text="Обучающие материалы📚"
        )
        # ,
        # KeyboardButton(
        #     text="Посты📰"
        # )
    ]
], one_time_keyboard=True, input_field_placeholder="Choice a button", selective=True)


# Кнопки для пунктов приема
towns_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="ХАНТЫ-МАНСИЙСК🌁"
        ),
        KeyboardButton(
            text="НИЖНЕВАРТОВСК🌁"
        ),
        KeyboardButton(
            text="СУРГУТ🌁"
        )
    ],
    [
        KeyboardButton(
            text="В главное меню⤵️"
        )
    ]
], one_time_keyboard=True, input_field_placeholder="Choice a button", selective=True)


# Кнопки для обучающих материалов
education_keyboard = ReplyKeyboardMarkup(keyboard=[
    # [
    #     KeyboardButton(
    #         text="Инфографика📑"
    #     ),
    #     KeyboardButton(
    #         text="Полезные ссылки🔗"
    #     ),
    #     KeyboardButton(
    #         text="Тест🏆"
    #     )
    # ],
    [
        # KeyboardButton(
        #     text="Экоурок🏫"
        # ),
        KeyboardButton(
            text="Интересные факты⭐️"
        )
    ],
    [
        KeyboardButton(
            text="В главное меню⤵️"
        )
    ]
], one_time_keyboard=True, input_field_placeholder="Choice a button", selective=True)


