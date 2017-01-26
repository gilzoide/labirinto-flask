# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, redirect, jsonify

from labirinto.sala import get_salas

from urllib import unquote


salas_blueprint = Blueprint('salas_blueprint', __name__)
SALAS = get_salas()


@salas_blueprint.route('/<int:num>')
def visita_sala(num):
    sala = SALAS[num]
    return render_template('sala.html', sala=sala)


@salas_blueprint.route('/<int:num>/<path:porta>')
def entra_porta(num, porta):
    porta = unquote(porta)
    sala = SALAS[num]
    proxima = sala.porta_proxima(porta)
    if proxima is not None:
        return redirect('/{}'.format(proxima))
    else:
        return jsonify(['Não achei porta', repr(sala), porta])


@salas_blueprint.route('/todas-salas')
def todas_salas():
    return render_template('todas-salas.html', todas_salas=SALAS)
