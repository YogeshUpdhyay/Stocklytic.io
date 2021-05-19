import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'i5Nvj87eblsuzqWVjLGA'
    RESTPLUS_MASK_SWAGGER = False
    TEMPLATE_DIR = "templates"
    STATIC_DIR = "static"
    
    # oauth2 configuration
    GOOGLE_CLIENT_ID= os.environ.get("GOOGLE_CLIENT_ID") or ""
    GOOGLE_CLIENT_SECRET= os.environ.get("GOOGLE_CLIENT_SECRET") or ""

    @staticmethod
    def init_app(app):
        pass

class TestConfig(Config):
    DEBUG = True
    TESTING = False

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