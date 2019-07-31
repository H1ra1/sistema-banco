from random import randint

def gerar_numero():
    numero = f'{randint(1000, 9999)}-{randint(1, 9)}'
    return numero

