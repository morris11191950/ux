from flask import Flask
from flaskext.mysql import MySQL
from config import app_config

db = MySQL()

app = Flask(__name__)

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)

    from app import models

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .literature import literature as literature_blueprint
    app.register_blueprint(literature_blueprint)

    from .trading_post import trading_post as trading_post_blueprint
    app.register_blueprint(trading_post_blueprint)

    from .prospects import prospects as prospects_blueprint
    app.register_blueprint(prospects_blueprint)

    return app
