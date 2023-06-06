
""" Calculadora com while """

while True:

    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')
    operador = input('Informe um operador (+-/*): ')

    nums_validos = None

    try:
        num_1_conv = float(num_1)
        num_2_conv = float(num_2)
        nums_validos = True
    except Exception as error:
        print(error)

    if (nums_validos is None):
        print('Por favor verifique se os números informados são válidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando o calculo. Confira o resultado abaixo: ')

    if operador == '+':
        print(f'{num_1_conv} + {num_2_conv} = ', num_1_conv + num_2_conv)
    elif operador == '-':
        print(f'{num_1_conv} - {num_2_conv} = ', num_1_conv - num_2_conv)
    elif operador == '/':
        print(f'{num_1_conv} / {num_2_conv} = ', num_1_conv / num_2_conv)
    elif operador == '*':
        print(f'{num_1_conv} * {num_2_conv} = ', num_1_conv * num_2_conv)
    else:
        print('Ops algo de errado')


    sair = input('Desja sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break

