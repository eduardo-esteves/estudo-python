"""
Introdução às funções (def) em Python
Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""


def somar(x, y, z):
    print(f'{x=}, y={y}, {z=}, | x + y + z = {x + y + z}')


print(somar)
somar(1, 2, 3)
somar(1, z=3, y=2)
