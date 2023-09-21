# aula 177

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Para filtrar posso usar list comprehension
precos_maiores_cinquenta = [
    p for p in produtos if p['preco'] > 50
]

# Neste exemplo usei uma função lambda como primeiro argumento de filter
# em seguida passei o valor interavel note que o resultado é o mesmo porém
# aqui está mais no estilo de programação funcional.
produtos_maiores_vinte = filter(
    lambda p: p['preco'] > 20,
    produtos
)

print_iter(produtos_maiores_vinte)


for produto in precos_maiores_cinquenta:
    print(f"Produto: {produto['nome']}, Preço: {produto['preco']}")
