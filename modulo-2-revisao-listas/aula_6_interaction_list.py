from helper.print_msg_section import print_msg_section


# PCP 36
pessoas = ['Vitor', 'Danny', 'Larissa', 'Edilene', 'Patricia', 'João', 'Maria', 'Eduardo']
pessoas_ini_e = []

for pessoa in pessoas:
    if 'e'.upper() in pessoa:
        pessoas_ini_e.append(pessoa)

print_msg_section('Pessoas que começam com a letra E')
print(pessoas_ini_e)


# A mesma lógica de for com List Comprehension
print_msg_section('A mesma lógica com List Comprehension')

novaLista = [pessoa for pessoa in pessoas if 'e'.upper() in pessoa]

print(novaLista)
