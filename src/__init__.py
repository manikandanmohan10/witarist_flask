from flask import Flask
from src.config.config import Config
from src.config.db import db
from flask_middleware import Middleware
from flask_migrate import Migrate
from src.common.blueprint import blueprints
from src.common.models import models_list
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    #Cors config
    CORS(app, resources={r"/*": {"origins": "*"}})

    #Config
    config = Config()
    app.config.from_object(config)

    # Registering Blueprints
    [app.register_blueprint(bp) for bp in blueprints]

    #Migrating Models
    Migrate(app, db)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app