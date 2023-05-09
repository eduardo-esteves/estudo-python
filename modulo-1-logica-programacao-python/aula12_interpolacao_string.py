"""
Interpolação básica de strings

s => string
d e i => int
f => float
x e X => Hexadecimal (ABCDE1234567890)
"""

nome = 'Eduardo'
preco = 100.00000

variavel = ' %s,o preço é R$%.2f' % (nome, preco)
hexadecimal = f'O hexadecimal de %d é %08X' % (1500, 1500)

print(variavel, '\n', hexadecimal)
