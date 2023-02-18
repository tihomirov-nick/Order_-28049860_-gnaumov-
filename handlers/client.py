from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from create_bot import bot
from keyboards import kb_client, kb_client_mini, kb_back
from data_base import sqlite_db

chat_id = -1001762432581


class Client_data(StatesGroup):
    category = State()
    text = State()
    user_name = State()


async def prestart_sending(message: types.Message):
    await state.finish()
    if str(message.from_user.last_name) == 'None':
        await bot.send_message(message.from_user.id,
                               text=f'Здравствуйте {message.from_user.first_name}, рады приветствовать Вас!',
                               reply_markup=kb_client_mini)
    else:
        await bot.send_message(message.from_user.id,
                               text=f'Здравствуйте {message.from_user.first_name} {message.from_user.last_name}, рады приветствовать Вас!',
                               reply_markup=kb_client_mini)
    await bot.send_message(message.from_user.id, text='Выберите категорию',
                           reply_markup=kb_client)
    await Client_data.next()


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Главное меню', reply_markup=kb_client)
    await bot.send_message(message.from_user.id, text='Выберите категорию',
                           reply_markup=kb_client)
    await Client_data.next()


async def start_sending(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['user_name'] = message.from_user.username
        data['category'] = message.text
    await bot.send_message(message.from_user.id, text='Введите текст обращения', reply_markup=kb_back)
    await Client_data.next()


async def end_sending(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
    await sqlite_db.sql_add_command(state)
    await bot.send_message(chat_id,
                           text=f'Пользователь {message.from_user.first_name}\nВ категории: ' + str(
                               data['category']) + '\nЗадал вопрос: ' + str(
                               data['text']) + '\nhttps://t.me/' + str(data['user_name']))
    await bot.send_message(message.from_user.id, text='Спасибо за ответ!\nК вам подключается специалист...',
                           reply_markup=kb_client)
    await state.finish()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(prestart_sending, commands=['start'], state=None)
    dp.register_message_handler(cancel_handler, state="*", text='Назад')
    dp.register_message_handler(start_sending, state=Client_data.category)
    dp.register_message_handler(end_sending, state=Client_data.text)
