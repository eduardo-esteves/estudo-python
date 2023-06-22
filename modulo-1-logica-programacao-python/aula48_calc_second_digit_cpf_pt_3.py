"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf: str = '74682489070'
cpf_calc: str = cpf[:9]
accumulator: int = 0
i: int = 10

for digito in cpf_calc:
    accumulator += int(digito) * i
    i -= 1

first_digit = (accumulator * 10) % 11
first_digit = 0 if first_digit > 9 else first_digit

print(f' A soma dos 9 primeiros digitos é {accumulator} e o calculo do primeiro digito do CPF é: {first_digit}')

"""
# Segunda parte do calculo do segundo digito
"""

cpf_calc = cpf[:9] + str(first_digit)
accumulator_2: int = 0
k: int = 11

for digito in cpf_calc:
    accumulator_2 += int(digito) * k
    k -= 1

second_digit: int = (accumulator_2 * 10) % 11
second_digit = 0 if second_digit > 9 else second_digit

print(f' A soma dos 9 primeiros digitos é {accumulator_2} e o calculo do segundo digito do CPF é: {second_digit}')


"""
# Terceira e última parte, validando se o CPF do cliente é válido
"""

cpf_gerado: str = f'{cpf[:9]}{str(first_digit)}{str(second_digit)}'

if cpf == cpf_gerado:
    print('O CPF informado é válido!')
else:
    print('O CPF informado é inválido!')
