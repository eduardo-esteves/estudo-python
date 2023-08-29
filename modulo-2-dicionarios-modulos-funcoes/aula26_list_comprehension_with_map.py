# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

#novos_produtos = [produto for produto in produtos]

# Aqui eu posso usar a list comprehension (Map) desempacotando cada valor do objeto alterando seu valor do preço.
novos_produtos = [{**produto, 'preco': produto['preco'] * 1.10} for produto in produtos]

# E só para facilitar, podemos ainda desempacotar cada objeto da lista e imprimir com uma quebra de linha
print(*novos_produtos, sep='\n')
