# -*- coding: utf-8 -*-

from flask import Blueprint, request, redirect, render_template, jsonify, abort

from labirinto.modelos import Sessao
from labirinto.db import DoesNotExist, MultipleObjectsReturned


sessoes_blueprint = Blueprint('sessoes', __name__)


@sessoes_blueprint.route('/sessao', methods=['POST'])
def sessao():
    data = request.form.to_dict()
    nome = data.get('nome')
    if not nome:
        return redirect('/')
    if data.get('salvar'):
        # descobre de qual sala veio através da requisição HTTP
        origin = request.headers['Origin']
        url = request.headers['Referer'][len(origin):]
        salva(nome, url)
        return render_template('salvou-sessao.html', nome=nome)
    elif data.get('carregar'):
        url = carrega(nome)
        if url:
            return redirect(url)
        else:
            return render_template('sessao-inexistente.html'), 404
    else:
        abort(400)


def salva(nome, url):
    Sessao.objects.upsert_one(nome=nome, url=url)


def carrega(nome):
    try:
        sess = Sessao.objects.get(nome=nome)
        return sess.url
    except DoesNotExist:
        return None


@sessoes_blueprint.route('/todas-sessoes')
def todas_sessoes():
    sessoes = Sessao.objects.all()
    return jsonify(list(sessoes))
