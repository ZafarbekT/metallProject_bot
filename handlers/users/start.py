from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

import json
from keyboards.inline.lang import language
from keyboards.default.menu_buttons import menu_all
from api import *

from loader import dp, _


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    data = await user_post(message.from_user.id, message.from_user.id)

    if data:
        markup = await language()
        await message.answer("Tilni tanlang / Выберите язык👇!", reply_markup=markup)
    else:
        markup = await menu_all(_)
        await message.answer(_("Qiziqish toifasini tanlang👇"), reply_markup=markup)
