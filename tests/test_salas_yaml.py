# -*- coding: utf-8 -*-

import unittest
from mock import patch
import yaml

from labirinto.sala import Sala, get_salas


salas_yaml = r"""
---
titulo: FIM DE JOGO
dica: Game Over, seu otario!
portas:
  - nome: Inicio
    proxima: ''
---
dica: Bom dia, senhor(a). Você conhece a lenda do labirinto?
portas:
  - nome: sim
    proxima: 3
  - nome: nao
    proxima: 2
---
dica: Era uma vez... cansei de história
portas:
  - nome: Tá na hora do pau
    proxima: 4
  - nome: Por favor, mais história
    proxima: 3
---
dica: Um frango xadrez, que na janta me satisfez. Tá satisfeito também?
portas:
  - nome: sim, sim, digo bora
    proxima: 4
---
dica: Ainda não há mais portas. Passar bem
portas: []
"""


class SalasTest(unittest.TestCase):
    """Testa a leitura de salas do arquivo YAML e seu conteúdo"""

    @patch('yaml.load_all', return_value=yaml.load_all(salas_yaml))
    def test_conteudo_yaml(self, mock_load_all):
        # número de salas
        self.assertEqual(Sala.num, -1)
        salas = get_salas()
        mock_load_all.assert_called_once()
        self.assertEqual(Sala.num, len(salas) - 1)

        # um pouco de conteúdo
        self.assertEqual(len(salas), 5)
        self.assertEqual(salas[0].titulo, 'FIM DE JOGO')
        self.assertFalse(salas[-1].portas)
        self.assertEqual(salas[1].titulo, "Sala 1")

        # próxima porta
        self.assertEqual(salas[1].porta_proxima('sim'), 3)
        self.assertEqual(salas[1].porta_proxima('nao'), 2)
        self.assertIsNone(salas[1].porta_proxima('nao existe'))
