import os
from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from authlib.integrations.flask_client import OAuth
from loginpass import create_flask_blueprint
from loginpass import GitHub, Google

from config import config

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()

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
    # intializing login manager
    login_manager.init_app(app)

def mailInit(app):
    mail.init_app(app)

def oauth2(app):
    # oauth2 for google and github
    from .utils.oauth2 import handle_authorize
    oauth = OAuth(app)
    bp = create_flask_blueprint([GitHub, Google], oauth, handle_authorize)
    app.register_blueprint(bp, url_prefix='/oauth2')

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

    # initializing login manager
    loginManager(app)

    # initializing mail extension
    mailInit(app)

    # configure OAuth2 
    oauth2(app)

    migrate = Migrate(app, db)

    # registering blueprints
    from .auth.routes import bp as auth_blueprint
    from .dashboard.routes import bp as dash_blueprint
    from .dashboard.api import bp as dash_api_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(dash_blueprint)
    app.register_blueprint(dash_api_blueprint)

    return app
