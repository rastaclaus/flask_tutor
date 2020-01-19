# pylint: disable=missing-module-docstring,missing-function-docstring
# pylint: disable=invalid-name

from pathlib import Path

from flask import Flask

from flaskr.db import db
from flaskr.models import migrate

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    instance_path = Path(app.instance_path)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=f'sqlite:///{instance_path / "flaskr.sqlite"}',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    if not instance_path.exists():
        instance_path.mkdir()

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
