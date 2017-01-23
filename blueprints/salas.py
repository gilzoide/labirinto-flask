# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, redirect

from sala import get_salas


salas_blueprint = Blueprint('salas', __name__)
SALAS = get_salas()


@salas_blueprint.route('/<int:num>')
def visita_sala(num):
    sala = SALAS[num]
    return render_template('sala.html', sala=sala)


@salas_blueprint.route('/<int:num>/<porta>')
def entra_porta(num, porta):
    sala = SALAS[num]
    proxima = sala.porta_proxima(porta)
    return redirect('/{}'.format(proxima))