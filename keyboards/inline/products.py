from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from api import *

async def products_func():
    products_btn = InlineKeyboardMarkup(row_width=2)

    data = await product_get()

    for item in data:
        products_btn.insert(InlineKeyboardButton(text=item['title'], callback_data=f"product_{item['id']}"))

    return products_btn
    