from helper.print_msg_section import print_msg_section


# PCP 34
pessoas = ['Vitor', 'Danny', 'Larissa', 'Patricia', 'João', 'Maria', 'Eduardo']
pessoas_2 = ['Lucas', 'Flávio']

# Posso remover pela chave
pessoas.remove('Vitor')
# Remover o último elemento
pessoas.pop()
# E ainda com pop() posso especificar o indice que desejo remover
pessoas.pop(0)
# E semelhante ao remove() posso remover através do indice
del pessoas[-2]

print(pessoas)

# Ainda com o uso de del posso deletar uma lista e para isso basta
# não passar o indice que pessoas vai deixar de existir, então uma
# excessão será lançada NameError não está definida.
del pessoas

# print(pessoas)

print_msg_section('Após limpar os itens uma lista vazia será impressa')
# E também posso remover todos os itens dentro de uma lista
pessoas_2.clear()
print(pessoas_2)
