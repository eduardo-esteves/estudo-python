from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

# Para zippar usando a lista menor posso usar zip()
result1 = list(zip(l1, l2))
print(result1)

print()

# Posso usar fillvalue para preencher um valor padrão que está sendo preenchido por None.
result2 = list(zip_longest(l1, l2, fillvalue='Sem Cidade'))
print(result2)
