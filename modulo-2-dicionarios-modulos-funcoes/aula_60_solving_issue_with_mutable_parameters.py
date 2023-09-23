
# Aula 191 Solução

# Resolvido o problema anterior de parâmetro mutável como default
# em argumento de funções, como None é um valor imutável já é
# suficiente bastando adicionar uma condição para se criar uma lista.
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('Eduardo')
adiciona_clientes('Joana', cliente1)

print(cliente1)

cliente2 = adiciona_clientes('Vitor')
adiciona_clientes('Maria', cliente2)

print(cliente2)
print(cliente1)
