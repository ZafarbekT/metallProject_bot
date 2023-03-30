from aiogram import types
from loader import dp, _, bot
from api import product_get_by_id, info_get
from aiogram.dispatcher.filters import Text

@dp.callback_query_handler(Text(startswith='product_'))
async def product_func(call: types.CallbackQuery):
    idx = call.data.index('_')
    index = call.data[idx+1:]
    product = await product_get_by_id(index)
    data = await info_get()
    if data == []:
        await call.message.answer("Malumotlar kiritilmagan!")
    else:
        img = 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fmiro.medium.com%2Fv2%2Fresize%3Afit%3A1400%2F1*m0H6-tUbW6grMlezlb52yw.png&tbnid=2aAp8YQnIZ1U6M&vet=12ahUKEwi216ek94L-AhXulIsKHfnmAQwQMygCegUIARDZAQ..i&imgrefurl=https%3A%2F%2Ftowardsdatascience.com%2Fthe-zen-of-python-a-guide-to-pythons-design-principles-93f3f76d088a&docid=EfkrW2Mo1yyPpM&w=1400&h=607&q=python&ved=2ahUKEwi216ek94L-AhXulIsKHfnmAQwQMygCegUIARDZAQ'
        info = _("""
📩 Telegram orqali buyurtma qilish uchun : 
{} ga murojat qilishingiz mumkin. 

Telefon orqali buyurtma berish uchun:

☎️ {}

📌 Kanalga ulanish uchun linkni bosing.!!! 👇 👇 👇

{}
""").format(data[0]["admin_telegram_username"], data[0]["admin_phone_number"], data[0]['bot_username'])
        
        await call.bot.send_photo(call.from_user.id, photo=img, caption=info)