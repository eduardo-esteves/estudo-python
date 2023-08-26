# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)


pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# Desempacota os valores do dict pessoa
nome, sobrenome = pessoa.values()

print(f'{nome=}, {sobrenome=}')
print()

# Retorna um array de tuplas, [('nome', 'Aline'), ('sobrenome', 'Souza')]
itens = pessoa.items()

print(itens)
print()

# Já no desempacotamento vou ter as tuplas fora do array ('nome', 'Aline') ('sobrenome', 'Souza')
key_1, key_2 = pessoa.items()

print(key_1, key_2)

# Sabendo que posso ter cada indice do array em forma de tuplas posso iterar sobre cada tupla manipulando key, value
for key, valor in pessoa.items():
    print(f'key:{key}, value:{valor}')
