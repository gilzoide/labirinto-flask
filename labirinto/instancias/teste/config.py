# -*- coding: utf-8 -*-

TESTING = True

MONGODB_DB = 'sessoes-teste'
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

SECRET_KEY = 'minha eguinha pocoto - teste'
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = SECRET_KEY
SECURITY_REGISTERABLE = True

# admin mais facil, tirar no produção
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
SECURITY_CHANGEABLE = True
