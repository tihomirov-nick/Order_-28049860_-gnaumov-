from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_button = KeyboardButton('Наши клиенты')
kb_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_admin.add(admin_button)