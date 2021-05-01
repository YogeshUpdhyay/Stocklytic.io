import os
from flask import Flask
from flask_cors import CORS
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def dbInit(app):
    # initializing database
    db.init_app(app)

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def loginManager(app):
    login_manager.init_app(app)

def create_app(config_name):
    # initializing app
    appconf = config[config_name]
    app = Flask(
        __name__,
        template_folder=os.path.join(os.getcwd(), appconf.TEMPLATE_DIR),
        static_folder=os.path.join(os.getcwd(), appconf.STATIC_DIR),
    )
    app.config.from_object(appconf)

    # enabling CORS
    CORS(app)

    # configuring database
    dbInit(app)

    # registering blueprints
    from .routes import auth, dashboard, stock
    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(stock.bp)

    return app
