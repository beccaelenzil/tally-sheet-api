from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    # __name__ store the name of the module we're in
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config is None:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DEV_DB')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TEST_DB')

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.member_routes import member_bp, root_bp
    app.register_blueprint(member_bp)
    app.register_blueprint(root_bp)

    from .routes.sheet_routes import sheet_bp
    app.register_blueprint(sheet_bp)

    from .routes.item_routes import item_bp
    app.register_blueprint(item_bp)


    from app.models.member import Member
    from app.models.sheet import Sheet
    from app.models.item import Item

    return app