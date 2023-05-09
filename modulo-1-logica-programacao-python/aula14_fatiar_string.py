"""
Fatiamento de strings
 012345678
 Olá mundo
 -987654321
Fatiamento [i:f:p] [::] => i=init, f=final, p=pass
Obs.: a função len retorna a qtd de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[4:])
print(variavel[-5:])
print(variavel[0])


print(f'O comprimento da string variável é: {len(variavel)}')
# O mesmo que 0:9
print(variavel[0:len(variavel):1])
# Imprime na ordem inversa devido ao passo negativo
print(variavel[-1::-1])

