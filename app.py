# -*- coding: utf-8 -*-

from flask import *

from blueprints.salas import salas_blueprint
from blueprints.sessao import sessao_blueprint
from db import db, DB_URI


# App e blueprints
app = Flask('labirinto')
app.register_blueprint(salas_blueprint)
app.register_blueprint(sessao_blueprint)
# Configurações
app.config['DATASET_DATABASE_URI'] = DB_URI
app.config['SECRET_KEY'] = "minha eguinha pocoto"


@app.route('/')
def index():
    session['pagina'] = '/'
    return render_template('index.html')


db.init_app(app)
app.run(debug=True, use_reloader=True)
