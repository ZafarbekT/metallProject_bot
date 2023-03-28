from aiogram import types
from loader import dp, _
from keyboards.default.menu_buttons import menu_uz, menu_ru
from api import put_lang

@dp.callback_query_handler(text="uz")
async def lang_function(call: types.CallbackQuery):
    await put_lang(call.from_user.id, "uz")
    markup = await menu_uz(_)
    await call.message.answer("Qiziqish toifasini tanlang👇", reply_markup=markup)

@dp.callback_query_handler(text="ru")
async def lang_function(call: types.CallbackQuery):
    await put_lang(call.from_user.id, "ru")
    markup = await menu_ru()
    await call.message.answer("Выберите интересующую категорию👇", reply_markup=markup)

