x = ("Gabriel", "Danny", "Arthur", "Danny")

# Para poder alterar os valores de uma tupla podemos fazer o
# seu cast para list e alterar o seus valores e depois fazer
# o cast novamente para o tipo tuple.
y = list(x)

# Adiciono Eduardo ao final da lista
y.append('Eduardo')
# Uma vez feita as alterações desejadas devo fazer o cast para tuple novamente
x = tuple(y)

print(y)
print(x)

print()
print('#' * 60 + ' Removendo valores de uma tupla ' + '#' * 60)
print()

z = list(x)
z.remove('Danny')
x = tuple(z)

print(x)
