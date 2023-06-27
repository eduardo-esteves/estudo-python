# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.

def multiplicaSum(*args):
    total = 1
    for num in args:
        total *= num if num > 0 else 1
    return total


total = multiplicaSum(1, 2, 3, 4, 0)

print(f' O total da multiplicação é: {total}')

