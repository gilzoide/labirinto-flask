# -*- coding: utf-8 -*-

from flask import Blueprint, request, redirect
from db import db


sessao_blueprint = Blueprint('sessao', __name__)


@sessao_blueprint.route('/sessao', methods=['POST'])
def sessao():
    data = request.form.to_dict()
    nome = data.get('nome')
    if data.get('salvar'):
        salva(nome, request.url_root)
    else:
        url = carrega(nome)
        return redirect(url)
    return redirect('/')


def salva(nome, url):
    print nome, url
    db['sessoes'].insert({'nome': nome, 'url': url})


def carrega(nome):
    sess = db['sessoes'].find_one(nome=nome)
    print sess['url']
    return sess['url']
