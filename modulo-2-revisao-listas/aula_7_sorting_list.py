from helper.print_msg_section import print_msg_section


# PCP 36
pessoas = ['Vitor', 'Danny', 'Larissa', 'Edilene', 'Patricia', 'João', 'Maria', 'Eduardo']

print(pessoas)

print_msg_section('Criando uma nova lista ordenada')
pessoas_ord = sorted(pessoas, reverse=True)

print(pessoas_ord)

print_msg_section('Ordena pessoas em ordem alfabetica ASC')

pessoas.sort()
print(pessoas)

print_msg_section('Ordena pessoas em ordem alfabetica DESC')

pessoas.sort(reverse=True)
print(pessoas)



