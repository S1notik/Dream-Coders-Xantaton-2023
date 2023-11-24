from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



# Кнопки для полезных ссылок
useful_links_buttons = [
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
            text="ВКонтакте👀",
            url="https://vk.com/eco4u2"
        ),
        InlineKeyboardButton(
            text="Телеграмм🕊️",
            url="https://t.me/yugraecology"
        ),
        InlineKeyboardButton(
            text="Одноклассники👋",
            url="https://ok.ru/group/55933980573950"
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

# Кнопки для Экоурока
ecolesson_buttons = [
        [
            InlineKeyboardButton(
                text="Записаться на Экоурок♻️",
                url="https://sobiraet.yugra-ecology.ru/form"),
        ]
]
ecolesson_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=ecolesson_buttons,
                                resize_keyboard=True,
                                one_time_keyboard=True,
                                input_field_placeholder="Choice a button",
                                selective=True)



# Кнопки для инфографии
quetion1_buttons = [
        [
            InlineKeyboardButton(
                text="Батарейки",
                callback_data="battery_infography")
        ],
        [
            InlineKeyboardButton(
                text="Бумага",
                callback_data="paper_infography")
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
        ],
        [
            InlineKeyboardButton(
                text="Что содержит мусорное ведро?",
                callback_data="what_is_contain_bin_infography")
        ],
        [
            InlineKeyboardButton(
                text="Ответственное потребление",
                callback_data="responsible_consumption_infography")
        ]
    ]
infography_keyboard = InlineKeyboardMarkup(inline_keyboard=quetion1_buttons,
                                           resize_keyboard=True,
                                           one_time_keyboard=True,
                                           input_field_placeholder="Choice a button",
                                           selective=True)



# Кнопки для вопросов теста-----------------------

# Вопрос первый
question1_buttons = [
        [
            InlineKeyboardButton(
                text="Материал упаковки может быть переработан или упаковка частично/полностью сделана из вторсырья",
                callback_data="answer1_question1_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Производитель уплатил лицензионный сбор и профинансировал сбор и сортировку отходов упаковки",
                callback_data="answer2_question1_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Это экологически безопасный продукт",
                callback_data="answer3_question1_quiz")
        ]
    ]
question1_keyboard = InlineKeyboardMarkup(inline_keyboard=question1_buttons,
                                           resize_keyboard=True,
                                           one_time_keyboard=True,
                                           input_field_placeholder="Choice a button",
                                           selective=True)


# Вопрос второй
question2_buttons = [
        [
            InlineKeyboardButton(
                text="Можно, и мыть необязательно",
                callback_data="answer1_question2_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Можно, и мыть необязательно",
                callback_data="answer2_question2_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Конечно, только предварительно его надо помыть",
                callback_data="answer3_question2_quiz")
        ]
    ]
question2_keyboard = InlineKeyboardMarkup(inline_keyboard=question2_buttons,
                                           resize_keyboard=True,
                                           one_time_keyboard=True,
                                           input_field_placeholder="Choice a button",
                                           selective=True)


# Вопрос третий
question3_buttons = [
        [
            InlineKeyboardButton(
                text="Долг останется только за тем, кто допустил просрочку платежа",
                callback_data="answer1_question3_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Долг распределят между всеми жильцами дома",
                callback_data="answer2_question3_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Долг распределят между всеми жильцами подъезда",
                callback_data="answer3_question3_quiz")
        ]
    ]
question3_keyboard = InlineKeyboardMarkup(inline_keyboard=question3_buttons,
                                           resize_keyboard=True,
                                           one_time_keyboard=True,
                                           input_field_placeholder="Choice a button",
                                           selective=True)


# Вопрос четвертый
question4_buttons = [
        [
            InlineKeyboardButton(
                text="Обычно я покупаю пластиковые тарелки, стаканы и вилки.",
                callback_data="answer1_question4_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Обычно я во время прогулок на природе не ем.",
                callback_data="answer2_question4_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Обычно я беру тарелки и стаканы из дома, чтобы после прогулки помыть их на кухне.",
                callback_data="answer3_question4_quiz")
        ]
    ]
question4_keyboard = InlineKeyboardMarkup(inline_keyboard=question4_buttons,
                                           resize_keyboard=True,
                                           one_time_keyboard=True,
                                           input_field_placeholder="Choice a button",
                                           selective=True)


# Вопрос пятый
question5_buttons = [
        [
            InlineKeyboardButton(
                text="Только хозяин квартиры на правах собственника",
                callback_data="answer1_question5_quiz")
        ],
        [
            InlineKeyboardButton(
                text="В зависимости от договоренностей хозяина и арендатора",
                callback_data="answer2_question5_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Только тот, кто снимает жилье",
                callback_data="answer3_question5_quiz")
        ]
    ]
question5_keyboard = InlineKeyboardMarkup(inline_keyboard=question5_buttons,
                                           resize_keyboard=True,
                                           one_time_keyboard=True,
                                           input_field_placeholder="Choice a button",
                                           selective=True)


# Вопрос шестой
question6_buttons = [
        [
            InlineKeyboardButton(
                text="Я каждый день покупаю 1,5 литровую бутылку питьевой воды.",
                callback_data="answer1_question6_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Я каждое утро беру с собой термос с питьевой водой.",
                callback_data="answer2_question6_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Я обычно за день могу купить 5 или 6 бутылок с разными напитками по 0,3 литра.",
                callback_data="answer3_question6_quiz")
        ]
    ]
question6_keyboard = InlineKeyboardMarkup(inline_keyboard=question6_buttons,
                                           resize_keyboard=True,
                                           one_time_keyboard=True,
                                           input_field_placeholder="Choice a button",
                                           selective=True)


# Вопрос седьмой
question7_buttons = [
        [
            InlineKeyboardButton(
                text="В офис агентов по расчетно-кассовому обслуживанию",
                callback_data="answer1_question7_quiz")
        ],
        [
            InlineKeyboardButton(
                text="В офис АО «Югра-Экология»",
                callback_data="answer2_question7_quiz")
        ],
        [
            InlineKeyboardButton(
                text="В офис своей управляющей компании",
                callback_data="answer3_question7_quiz")
        ]
    ]
question7_keyboard = InlineKeyboardMarkup(inline_keyboard=question7_buttons,
                                           resize_keyboard=True,
                                           one_time_keyboard=True,
                                           input_field_placeholder="Choice a button",
                                           selective=True)


# Вопрос восьмой
question8_buttons = [
        [
            InlineKeyboardButton(
                text="Светодиодные лампочки",
                callback_data="answer1_question8_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Консервные банки",
                callback_data="answer2_question8_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Батарейки",
                callback_data="answer3_question8_quiz")
        ]
    ]
question8_keyboard = InlineKeyboardMarkup(inline_keyboard=question8_buttons,
                                           resize_keyboard=True,
                                           one_time_keyboard=True,
                                           input_field_placeholder="Choice a button",
                                           selective=True)


# Вопрос девятый
question9_buttons = [
        [
            InlineKeyboardButton(
                text="Полиэтиленовый пакет",
                callback_data="answer1_question9_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Полиэтиленовый пакет",
                callback_data="answer2_question9_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Железная консервная банка",
                callback_data="answer3_question9_quiz")
        ]
    ]
question9_keyboard = InlineKeyboardMarkup(inline_keyboard=question9_buttons,
                                           resize_keyboard=True,
                                           one_time_keyboard=True,
                                           input_field_placeholder="Choice a button",
                                           selective=True)


# Вопрос десятый
question10_buttons = [
        [
            InlineKeyboardButton(
                text="Упаковка из прессованной макулатуры",
                callback_data="answer1_question10_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Упаковка из пластика",
                callback_data="answer2_question10_quiz")
        ],
        [
            InlineKeyboardButton(
                text="Упаковка из вспененного полистирола",
                callback_data="answer3_question10_quiz")
        ]
    ]
question10_keyboard = InlineKeyboardMarkup(inline_keyboard=question10_buttons,
                                           resize_keyboard=True,
                                           one_time_keyboard=True,
                                           input_field_placeholder="Choice a button",
                                           selective=True)


'''
question1_buttons = []
question2_buttons = []


list_buttons = [question1_buttons, question2_buttons]

file = open("data/text/quiz.txt", "r")
lines = file.readlines()
j = 1

for i in range(2):
    answers = lines[i].split("\\")[1].split("/")
    list_buttons[i] = [
        [
            InlineKeyboardButton(
                text=answers[0],
                callback_data="answer1_question" + str(i) + "_quiz")
        ],
        [
            InlineKeyboardButton(
                text=answers[1],
                callback_data="answer2_question" + str(i) + "_quiz")
        ],
        [
            InlineKeyboardButton(
                text=answers[2],
                callback_data="answer3_question" + str(i) + "_quiz")
        ]
    ]'''
