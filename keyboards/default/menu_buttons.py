from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.contrib.middlewares.i18n import I18nMiddleware

async def menu_uz(_: I18nMiddleware):

    buttons = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton('📃 Maxsulotlar')
            ],
            [
                KeyboardButton("📞 Biz bilan bog'laning"),
                KeyboardButton("⚙ Sozlash")
            ],
            [
                KeyboardButton("📍 Bizning Manzil")
            ]
        ], resize_keyboard=True
    )

    return buttons

async def menu_ru():
    buttons = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    buttons = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton('📃 Прайс')
            ],
            [
                KeyboardButton('📞 Свяжитесь с нами'),
                KeyboardButton('⚙ Настройки')
            ],
            [
                KeyboardButton('📍 Наше Локация')
            ]
        ], resize_keyboard=True
    )

    return buttons
