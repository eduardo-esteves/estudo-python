"""
Retorno de valores das funções (return)
"""


def soma(x, y, *args):
    if len(args) <= 0:
        return x + y
    total = x + y
    for num in args:
        total += num
    return total


soma1 = soma(4, 2)
soma2 = soma(3, 3, 10, 100)

print(soma1 + soma2)
print(soma(11, 55))
