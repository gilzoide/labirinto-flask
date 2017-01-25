# -*- coding: utf-8 -*-

import unittest
import yaml
try:
    import mock
except ImportError:
    from unittest import mock

from labirinto.sala import *


lista_salas = yaml.load(r"""
- titulo: FIM DE JOGO
  dica: Game Over, seu otario!
  portas:
    - nome: Inicio
      proxima: ''

- dica: Bom dia, senhor(a). Você conhece a lenda do labirinto?
  portas:
    - nome: sim
      proxima: 3
    - nome: nao
      proxima: 2

- dica: Era uma vez... cansei de história
  portas:
    - nome: Tá na hora do pau
      proxima: 4
    - nome: Por favor, mais história
      proxima: 3

- dica: Um frango xadrez, que na janta me satisfez. Tá satisfeito também?
  portas:
    - nome: sim, sim, digo bora
      proxima: 4

- dica: Ainda não há mais portas. Passar bem
  portas: []
""")


class SalasTest(unittest.TestCase):
    """Testa a leitura de salas do arquivo YAML e seu conteúdo"""

    @mock.patch('labirinto.sala.yaml.load', autospec=True)
    def test_conteudo_yaml(self, mock_load):
        mock_load.return_value = lista_salas
        # número das salas
        self.assertFalse(mock_load.called)
        salas = get_salas()
        self.assertEqual(mock_load.call_count, 1)
        self.assertSequenceEqual(map(lambda s: s.num, salas), range(len(salas)))

        # um pouco de conteúdo
        self.assertEqual(len(salas), 5)
        self.assertEqual(salas[0].titulo, 'FIM DE JOGO')
        self.assertFalse(salas[-1].portas)
        self.assertEqual(salas[1].titulo, "Sala 1")

        # próxima porta
        self.assertEqual(salas[1].porta_proxima('sim'), 3)
        self.assertEqual(salas[1].porta_proxima('nao'), 2)
        self.assertIsNone(salas[1].porta_proxima('nao existe'))

        inicio = salas[0].porta_proxima('Inicio')
        self.assertEqual(inicio, '')
        self.assertIsNotNone(inicio)
