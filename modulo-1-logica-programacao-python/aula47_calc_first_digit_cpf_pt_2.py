"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

"""

cpf: str = '74682489070'
cpf_calc: str = cpf[:9]
acumlator: int = 0
i: int = 10

for digito in cpf_calc:
    acumlator += int(digito) * i
    i -= 1

first_digit = (301 * 10) % 11
first_digit = 0 if first_digit > 9 else first_digit

print(f' A soma dos 9 primeiros digitos é {acumlator} e o calculo do primeiro digito é {first_digit}')
