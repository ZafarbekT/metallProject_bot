from aiogram import types
from loader import dp, _
from keyboards.default.menu_buttons import menu_uz, menu_ru
from api import put_lang
from keyboards.inline.products import subscribe

@dp.callback_query_handler(text="uz")
async def lang_function(call: types.CallbackQuery):
    x = await subscribe()
    await call.message.answer("Yangiliklardan xabardor bo'lish uchun\nBizning kanalga obuna bo'ling👇", reply_markup=x)
    await put_lang(call.from_user.id, "uz")
    markup = await menu_uz(_)
    await call.message.answer("Qiziqish toifasini tanlang👇", reply_markup=markup)

@dp.callback_query_handler(text="ru")
async def lang_function(call: types.CallbackQuery):
    x = await subscribe()
    await call.message.answer("Подпишитесь на наш канал, чтобы быть в курсе новостей👇", reply_markup=x)
    await put_lang(call.from_user.id, "ru")
    markup = await menu_ru()
    await call.message.answer("Выберите интересующую категорию👇", reply_markup=markup)

