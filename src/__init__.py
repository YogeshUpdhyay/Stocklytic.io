import os
from flask import Flask
from flask_cors import CORS
from config import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Base = None
global Base

def dbInit():
    engine = create_engine('postgresql://root:example@db:5432/StockAnalyzerDB', echo=True)
    Base = declarative_base()  
    Base.metadata.create_all(engine)

def create_app(config_name):
    appconf = config[config_name]
    app = Flask(
        __name__,
        template_folder=os.path.join(os.getcwd(), appconf.TEMPLATE_DIR),
        static_folder=os.path.join(os.getcwd(), appconf.TEMPLATE_DIR),
        static_url_path="/static"
    )
    app.config.from_object(appconf)
    CORS(app)

    # DB configuration
    dbInit()

    # App routes
    from .routes import auth, dashboard, stock
    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(stock.bp)

    return app
