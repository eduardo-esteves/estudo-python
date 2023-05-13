"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite seu nome: ')
length_nome = len(nome)


if length_nome >= 3:
    if (length_nome <= 4):
        print('Seu nome é curto')
    elif (length_nome <= 6):
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite um nome com o minimo de três letras')
