# -*- coding: utf-8 -*-

from flask import *

from blueprints.salas import salas_blueprint
from blueprints.sessao import sessao_blueprint
from blueprints.index import index_blueprint
from db import db

from os import path


def create_app(modo='development'):
    instance_path = path.join(path.abspath(path.dirname(__file__)), 'instancias', modo)
    # App e blueprints
    app = Flask('labirinto', instance_path=instance_path, instance_relative_config=True)
    app.register_blueprint(salas_blueprint)
    app.register_blueprint(sessao_blueprint)
    app.register_blueprint(index_blueprint)
    # Configurações
    app.config.from_pyfile('config.py')
    db.init_app(app)
    return app
