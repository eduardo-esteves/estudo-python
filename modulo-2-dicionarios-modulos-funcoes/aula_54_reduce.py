# Aula 178
from functools import reduce


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.30},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.00},
]

total = 0

for p in produtos:
    total += p['preco']

print(round(total, 2))


def total_produtos(ac, produto):
    return ac + produto['preco']


#total = reduce(total_produtos, produtos, 0)
total = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(total)
