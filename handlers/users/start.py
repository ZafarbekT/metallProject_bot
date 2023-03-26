from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.lang import language

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    markup = await language()
    await message.answer("Tilni tanlang / Выберите язык👇!", reply_markup=markup)
