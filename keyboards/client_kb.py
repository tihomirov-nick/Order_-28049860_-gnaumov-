from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_button = KeyboardButton('Назад')
kb_back = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_back.add(back_button)

menu_button1 = KeyboardButton('Вам нужен сайт под ключ?')
menu_button2 = KeyboardButton('Вам нужно SEO продвижение?')
menu_button3 = KeyboardButton('Вам нужна контекстная Реклама?')
menu_button4 = KeyboardButton('Вам нужно все комплексом?')
menu_button5 = KeyboardButton('Вам нужно обучение?')
menu_button6 = KeyboardButton('Вам нужен копирайтинг?')
menu_button7 = KeyboardButton('Вам нужен дизайн?')
menu_button8 = KeyboardButton('У Вас вопрос?')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(menu_button1, menu_button2, menu_button3) \
    .add(menu_button4) \
    .add(menu_button5, menu_button6, menu_button7) \
    .add(menu_button8) \
    .add(back_button)

menu_button_mini = KeyboardButton('Услуги')
kb_client_mini = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_mini.add(menu_button_mini)

