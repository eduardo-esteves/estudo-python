from helper.print_msg_section import print_msg_section


# PCP 31
pessoas = ['Vitor', 'Danny', 'Larissa', 'Patricia', 'João', 'Maria', 'Eduardo']

# Verificando se um certo valor está dentro da lista
if 'Eduardo' in pessoas:
    print('Eduardo está dentro da lista de pessoas')

print_msg_section('Revertendo a ordem dos indices de uma lista')
pessoas.reverse()
print(pessoas)
