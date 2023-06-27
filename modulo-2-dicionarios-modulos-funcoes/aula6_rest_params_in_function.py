"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


numeros = (1, 2, 3, 4, 5, 6, 7, 78, 10)
# Fazendo o desempacotamento da tupla numeros na execução da função
outra_soma = soma(*numeros)

print(outra_soma)

print(sum(numeros))
