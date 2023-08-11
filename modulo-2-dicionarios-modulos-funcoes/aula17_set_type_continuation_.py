# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)


# s1 = {1, 2, 3}
# print(3 not in s1)
# for numero in s1:
#     print(numero)

# Eficiente para remover valores duplicados
l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1)

print(s1)
print()

# E fazer a conversão para lista novamente
l2 = list(s1)

print(l2)
print()

# Como são iteraveis
print(f'3 in s1: {3 in s1}')
print()

for number in s1:
    print(number)


