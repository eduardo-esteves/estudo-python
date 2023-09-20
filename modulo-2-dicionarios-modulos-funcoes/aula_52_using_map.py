# Aula 176
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


def aumentar_preco(valor):
    return {
        **valor,
        'preco': round((valor['preco'] * 1.10), 2)
    }


# Map precisa que o primeiro argumento seja uma função onde irá processar cada valor do interator
# produtos até que o iterator se esgote.
novos_produtos = map(aumentar_preco, produtos)

# Neste exemplo usei uma função lambda para centralizar a mesma lógica tudo em uma única linha
# para isso crio um novo dicionário para produto, e em seu preco faço o acrescimo de 10%.
produtos_acrescido_10_cento = list(map(
    lambda p: {'nome': p['nome'], 'preco': round(p['preco'] * 1.10, 2)},
    produtos
))

# print_iter(novos_produtos)

for produto in produtos_acrescido_10_cento:
    print(f"Nome: {produto['nome']}, Preço: {produto['preco']}")
