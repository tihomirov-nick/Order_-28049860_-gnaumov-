import sqlite3 as sq
from create_bot import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards import kb_admin


def sql_start():
    global base, cur
    base = sq.connect('USERID.db')
    cur = base.cursor()
    if base:
        print("DataBase connected")
    base.execute('CREATE TABLE IF NOT EXISTS main(id TEXT, category TEXT, text TEXT)')
    base.commit()


async def sql_add_command(state):
    try:
        async with state.proxy() as data:
            cur.execute("INSERT INTO main VALUES (?, ?, ?)", tuple(data.values()))
            base.commit()
    except:
        pass


async def sql_read_command(message):
    await bot.send_message(message.from_user.id, text=f"Клиенты, которые писали нам ранее.",
                           reply_markup=kb_admin)
    for ret in cur.execute('SELECT * FROM main'):
        await bot.send_message(message.from_user.id, text=f"{ret[1]}\n{ret[2]}",
                               reply_markup=InlineKeyboardMarkup().add(
                                   InlineKeyboardButton('Контакт', url=f'https://t.me/{ret[0]}')))
