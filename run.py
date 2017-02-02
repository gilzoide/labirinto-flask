#!/usr/bin/env python
# -*- coding: utf-8 -*-

from labirinto.app import create_app

from sys import argv
import os

modo = argv[1] if len(argv) > 1 else 'dev'
assert modo in os.listdir(os.path.join('labirinto', 'instancias')), "Modo de execução deve ser 'dev' ou 'teste'"
app = create_app(modo)
app.run(debug=True, use_reloader=True)
