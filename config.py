import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'i5Nvj87eblsuzqWVjLGA'
    RESTPLUS_MASK_SWAGGER = False
    TEMPLATE_DIR = "templates"
    STATIC_DIR = "static"
    
    # oauth2 configuration
    GOOGLE_CLIENT_ID= os.environ.get("GOOGLE_CLIENT_ID") or "512067544038-g0r87o90n52uilp000d9fhcg8f0tt0j6.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET= os.environ.get("GOOGLE_CLIENT_SECRET") or "uJmqgnbLe1MmFj0KjISfrIMH"

    @staticmethod
    def init_app(app):
        pass

class TestConfig(Config):
    DEBUG = True
    TESTING = False
    WTF_CSRF_ENABLED = False
    ERROR_404_HELP = False
    SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE =True
    RESTPLUS_MASK_SWAGGER = False

    SQLALCHEMY_DATABASE_URI = "postgresql://root:example@localhost/StockAnalyzerDB"
    RESET_EXPIRATION_TIME = 1800
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('EMAIL_USER') or ""
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD') or ""
    
class Production(Config):
    pass

config = {
    'debug': TestConfig,
    'production': Production
}