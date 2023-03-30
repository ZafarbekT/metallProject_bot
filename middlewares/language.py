from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware as BaseI18nMiddleware

from api import get_lang
# from loader import db
# from tgbot.service.repo.repository import SQLAlchemyRepos
# from tgbot.service.repo.user_repo import UserRepo
# from utils.db_api.sqlite import Database

# db = Database()


class I18nMiddleware(BaseI18nMiddleware):

    async def get_user_locale(self, action, data):
        user = types.User.get_current()
        db_language = await get_lang(id=user.id)

        if db_language:
            return db_language['lang']
        else:
            return user.locale