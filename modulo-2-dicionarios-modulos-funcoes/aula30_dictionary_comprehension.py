# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produto.items()
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]

# Crio um novo dictionary com base na minha lista de tupla
list_tuple = {
    chave: valor
    for chave, valor in lista
}

print(list_tuple)
