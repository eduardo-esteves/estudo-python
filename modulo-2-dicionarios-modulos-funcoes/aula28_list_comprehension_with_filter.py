# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20.0, },
    {'nome': 'p2', 'preco': 10.0, },
    {'nome': 'p3', 'preco': 30.0, },
]

# Posso também desempacotar cada dictionary da list e criar meu filtro com base na condição, note que a diferença
# de um map para filter é que no filter não temos um else e que a condição sempre vem após a instrução for.
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.10}
    for produto in produtos if produto['preco'] >= 20
]

# E só para facilitar, podemos ainda desempacotar cada objeto da lista e imprimir com uma quebra de linha
print(*novos_produtos, sep='\n')
