from aiogram import Dispatcher
# from loader import dp
from .throttling import ThrottlingMiddleware
from .language import I18nMiddleware

def setup_middlewares(dp: Dispatcher) -> None:
    dp.middleware.setup(I18nMiddleware(domain="messages", path="locales", default="uz"))
    dp.middleware.setup(ThrottlingMiddleware())