# -*- coding: utf-8 -*-

import yaml


class Sala:
    """Uma sala do labirinto, com um texto dica e as portas existentes, cada uma
    levando a outra sala"""
    def __init__(self, num, dica, portas, titulo=None):
        self.num = num
        self.dica = dica
        self.portas = portas
        self.titulo = titulo or "Sala {}".format(num)

    # número atual da sala, crescente, começando em 0 (ele dá ++ antes de criar)
    num = -1

    @classmethod
    def cria_sala(cls, dica, portas, titulo=None):
        cls.num += 1
        return cls(cls.num, dica, portas, titulo)

    def __repr__(self):
        return 'Sala({0.num}, {0.dica!r}, {0.portas!r}, {0.titulo!r})'.format(self)

    def porta_proxima(self, nome):
        """Acha qual o proximo passo a partir da porta"""
        # Usa `for` retornando o primeiro elemento pra funcionar tanto no python 2 quanto 3
        for porta in filter(lambda p: p['nome'] == nome, self.portas):
            return porta['proxima']


def get_salas():
    """Le o documento de salas e retorna a lista das salas existentes"""
    with open('salas.yml', 'r') as arq:
        docs = yaml.load_all(arq)
        salas = [Sala.cria_sala(**sala) for sala in docs]
        return salas
