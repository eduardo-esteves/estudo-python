from helper.print_msg_section import print_msg_section


# PCP 32
pessoas = ['Vitor', 'Danny', 'Larissa', 'Patricia', 'João', 'Maria', 'Eduardo']

# Verificando se um certo valor está dentro da lista
if 'Eduardo' in pessoas:
    print('Eduardo está dentro da lista de pessoas')

# Lembre-se que para atingir um indice de um intervalo final
# sempre devemos acrescentar + 1 ao alvo final isso devido o
# último indice informado sempre ser excluido da lista.
pessoas[1:3] = ['Janaina', 'Marta']

print_msg_section('Atualizando os valores do segundo e terceiro indice')
print(pessoas)

# Em caso de termos mais valores do que o limite informado então
# ao chegar neste limite, o restante dos valores serão inseridos
# na ordem logo o último valor da atualização, porém os restantes
# dos valores da lista não serão afetados.
pessoas[1:4] = ['Gabriela', 'Carlos', 'Leticia', 'Amanda', 'Jacqueline']

print_msg_section('Atualizando do segundo ao quarto elemento')
print(pessoas)

# Em casos também de passarmos uma quantidade menor que os valores correspondente
# ao intervalo então teremos a remoção de itens

pessoas[1:4] = ['Larissa']
print_msg_section('Neste caso Gabriela até Leticia será substituido por Larissa')
print(pessoas)

