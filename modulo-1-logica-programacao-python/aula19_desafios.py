"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if (hora >= 0 and hora <= 11):
        print('Bom dia 0-11')
    elif (hora >= 12 and hora <= 17):
        print('Bom tarde 12-17')
    elif (hora >= 18 and hora <= 23):
        print('Boa noite 18-23')
    else:
        print('A hora informada é desconhecida')
except:
    print('O valor digitado não é um número inteiro')
