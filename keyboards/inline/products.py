from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from api import *
from data.data import i18n


async def products_func(message):
    user_language = await i18n.get_user_locale(message, data=None)
    data = await product_get()

    products_btn = InlineKeyboardMarkup(row_width=2)

    for item in data:
        products_btn.insert(InlineKeyboardButton(text=item[f'title_{user_language}'], callback_data=f"product_{item['id']}"))

    return products_btn
    
async def subscribe():
    button = InlineKeyboardMarkup(
        inline_keyboard = [
            [
                InlineKeyboardButton(text="VendMetall", url="https://t.me/vendmetall")
            ],
        ],
    )
    return button

# Yangiliklardan xabardor bo'lish uchun\nBizning kanalga obuna bo'ling👇