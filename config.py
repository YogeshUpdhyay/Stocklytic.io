import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'i5Nvj87eblsuzqWVjLGA'
    RESTPLUS_MASK_SWAGGER = False
    TEMPLATE_DIR = "templates"
    STATIC_DIR = "static"

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
    SQLALCHEMY_DATABASE_URI = "postgresql://root:example@db/StockAnalyzerDB"

class Production(Config):
    pass

config = {
    'debug': TestConfig,
    'production': Production
}