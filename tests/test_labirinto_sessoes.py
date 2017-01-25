# -*- coding: utf-8 -*-

from labirinto.app import create_app
from labirinto.modelos import Sessao

import unittest
import json


class LabirintoTest(unittest.TestCase):
    """Testa uns trem loko aí do flask"""

    def setUp(self):
        self.app = create_app('teste').test_client()

    def tearDown(self):
        Sessao.drop_collection()

    def get_todas_sessoes(self):
        """Pega o resultado de um GET em /todas-sessoes e parseia o JSON"""
        rv = self.app.get('/todas-sessoes')
        return json.loads(rv.data)

    def pede_pra_salvar(self, nome, referer_sufixo):
        """Roda uma requisição de salvar, com uns parâmetros padrão"""
        base_url = 'labirinto-url'
        return self.app.post('/sessao', data={
            'nome': nome,
            'salvar': True,
        }, environ_overrides={
            'HTTP_ORIGIN': base_url,
            'HTTP_REFERER': base_url + referer_sufixo,
        })

    def me_carrega(self, nome, carregar=True):
        """Roda uma requisição POST pra carregar uma sessão.

        :param carregar: passe False pra requisição falhar com erro 400
        """
        return self.app.post('/sessao', data={
            'nome': nome,
            'carregar': carregar,
        })

    def test_nenhuma_sessao(self):
        # cabou de começar o BD, não tem sessão
        self.assertItemsEqual([], self.get_todas_sessoes())

    def test_salvar(self):
        # testa a requisição
        rv = self.pede_pra_salvar('teste', '/2')
        self.assertIn('Sessão salva com sucesso', rv.data)
        self.assertEqual(200, rv.status_code)

        # testa resultado
        sessoes = self.get_todas_sessoes()
        self.assertEqual(1, len(sessoes))
        self.assertEqual(sessoes[0]['url'], '/2')

        # salva mais uma nova
        self.pede_pra_salvar('teste2', '/5')
        sessoes = self.get_todas_sessoes()
        self.assertEqual(2, len(sessoes))

        # agora atualiza um deles, fazendo com que o número de sessões continue em 2
        self.pede_pra_salvar('teste', '/3')
        sessoes = self.get_todas_sessoes()
        self.assertEqual(2, len(sessoes))
        self.assertEqual(sessoes[0]['url'], '/3')

    def test_carrega(self):
        self.pede_pra_salvar('teste', '/2')

        # sessão que existe
        rv = self.me_carrega('teste')
        self.assertNotIn('Sessão não existe', rv.data)
        self.assertEqual(302, rv.status_code)

        # sessão que não existe
        rv = self.me_carrega('inexistente')
        self.assertIn('Sessão não existe', rv.data)
        self.assertEqual(404, rv.status_code)

        # requisição mal formada
        rv = self.me_carrega('teste', None)
        self.assertEqual(400, rv.status_code)
