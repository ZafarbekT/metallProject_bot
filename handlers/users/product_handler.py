from aiogram import types
from loader import dp, bot, _
from keyboards.inline.products import products_func
from api import info_get

@dp.message_handler(text=_('📃 Maxsulotlar', '📃 Прайс'))
async def product_function(message: types.Message):
    markup = await products_func()
    await message.answer('Mahsulotlar', reply_markup=markup)

@dp.message_handler(text=[_("📞 Biz bilan bog'laning"), '📞 Свяжитесь с нами'])
async def product_function(message: types.Message):
    data = await info_get()
    if data != []:
        info = _("""
📩 Telegram orqali buyurtma qilish uchun : 
{} ga murojat qilishingiz mumkin. 

Telefon orqali buyurtma berish uchun:

☎️ {}

📌 Kanalga ulanish uchun linkni bosing.!!! 👇 👇 👇

{}
""").format(data[0]["admin_telegram_username"], data[0]["admin_phone_number"], data[0]['bot_username'])
        await message.answer(info)
    else:
        await message.answer(_("Ma'lumot topilmadi!"))

@dp.message_handler(text=[_('📍 Bizning Manzil'), '📍 Наше Локация'])
async def product_function(message: types.Message):
    data = await info_get()
    if data != []:
        index = data[0]['location'].index(',')
        lon = data[0]['location'][index+1:].replace(' ', '')
        lat = data[0]['location'][:index]
        await bot.send_location(message.from_user.id, latitude=lat, longitude=lon)
    else:
        await message.answer(_("Manzil topilmadi!"))

