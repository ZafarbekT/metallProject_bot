from aiogram import types
from loader import dp
from keyboards.inline.lang import language

@dp.message_handler(text=["⚙ Sozlash", "⚙ Настройки"])
async def menu_function(message: types.CallbackQuery):
    markup = await language()
    await message.answer("Tilni tanlang / Выберите язык👇!", reply_markup=markup)
