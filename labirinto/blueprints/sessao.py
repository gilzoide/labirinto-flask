# -*- coding: utf-8 -*-

from flask import Blueprint, request, redirect, render_template, jsonify, abort

from labirinto.db import db


sessao_blueprint = Blueprint('sessao', __name__)


@sessao_blueprint.route('/sessao', methods=['POST'])
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
    db['sessoes'].upsert({'nome': nome, 'url': url}, ['nome'])


def carrega(nome):
    sess = db['sessoes'].find_one(nome=nome)
    return sess and sess['url']


@sessao_blueprint.route('/todas-sessoes')
def todas_sessoes():
    sessoes = db['sessoes'].all()
    return jsonify(list(sessoes))
