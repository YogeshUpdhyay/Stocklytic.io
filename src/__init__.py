import os
from flask import Flask
from flask_cors import CORS
from config import config

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

    # App routes
    from .routes import auth, dashboard
    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)

    return app
