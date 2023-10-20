from helper.print_msg_section import print_msg_section


# PCP 33
pessoas = ['Vitor', 'Danny', 'Larissa', 'Patricia', 'João', 'Maria', 'Eduardo']
pessoas_2 = ['Lucas', 'Flávio']

# Adiciono um novo valor ao final da lista
pessoas.append('Marizmar')
# Adiciono um novo valor a uma posição especifica
pessoas.insert(1, 'Jamilha')

print_msg_section('Juntando listas com extend()')
# Juntando objetos interaveis, pode ser tanto uma lista quanto tupla
# ou qualquer outro objeto interavel.
pessoas.extend(pessoas_2)
print(pessoas)

print_msg_section('Também posso juntar lista com concat')
# Concat neste caso é usado através do sinal de + ou seja aqui
# o Python está usando o recurso de polimorfismo
novas_pessoas = pessoas + pessoas_2
print(novas_pessoas)
