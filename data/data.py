from middlewares import I18nMiddleware

i18n = I18nMiddleware(domain="messages", path="locales", default="uz")