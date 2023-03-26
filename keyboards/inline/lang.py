from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def language():
    lang = InlineKeyboardMarkup(row_width=1)

    languages_dict = {
        "🇺🇿 O'zbek tili": "uz",
        "🇷🇺 Русский язык": "ru"
    }

    for key, value in languages_dict.items():
        lang.insert(InlineKeyboardButton(text=key, callback_data=value))

    return lang
    