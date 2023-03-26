from aiogram import types
from loader import dp
from keyboards.default.menu_buttons import menu_uz, menu_ru

@dp.callback_query_handler(text="uz")
async def lang_function(call: types.CallbackQuery):
    markup = await menu_uz()
    await call.message.answer("Qiziqish toifasini tanlang👇", reply_markup=markup)

@dp.callback_query_handler(text="ru")
async def lang_function(call: types.CallbackQuery):
    markup = await menu_ru()
    await call.message.answer("Выберите интересующую категорию👇", reply_markup=markup)

