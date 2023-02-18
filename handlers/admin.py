from aiogram import types, Dispatcher
from create_bot import bot
from data_base import sqlite_db
from keyboards import kb_admin

chat_id = -1001762432581


async def start_command_admin(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id, user_id=message.from_user.id)
    if user_channel_status["status"] != 'left':
        await bot.send_message(message.from_user.id,
                               text=f'Здравствуйте {message.from_user.first_name}, это панель администратора.',
                               reply_markup=kb_admin)
    else:
        await bot.send_message(message.from_user.id, 'Вы не являетесь администратором!')



async def show_clients(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id, user_id=message.from_user.id)
    if user_channel_status["status"] != 'left':
        await sqlite_db.sql_read_command(message)
    else:
        await bot.send_message(message.from_user.id, 'Вы не являетесь администратором!')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(start_command_admin, commands=['admin'])
    dp.register_message_handler(show_clients, text='Наши клиенты')
