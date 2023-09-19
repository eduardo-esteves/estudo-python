from itertools import combinations, permutations, product


# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

combinations_1 = combinations(pessoas, 2)
permutations_1 = permutations(pessoas, 2)
product_1 = product(*camisetas)

print_iter(combinations_1)
print_iter(permutations_1)
print_iter(product_1)
