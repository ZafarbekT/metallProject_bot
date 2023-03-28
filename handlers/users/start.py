from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

import json
from keyboards.inline.lang import language
from keyboards.inline.products import products_func
from api import *

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    telegram_id = message.from_user.id
    username = message.from_user.username

    data = await user_post(username, telegram_id)
    # print(data)

    product = await products_func()
    # print(product)

    lang = await get_lang(telegram_id)
    # print(lang)

    await put_lang(message.from_user.id, 'uz')

    lang1 = await get_lang(telegram_id)                                                                                                                                                                                     
    # print(lang1)

    markup = await language()
    await message.answer("Tilni tanlang / Выберите язык👇!", reply_markup=product)