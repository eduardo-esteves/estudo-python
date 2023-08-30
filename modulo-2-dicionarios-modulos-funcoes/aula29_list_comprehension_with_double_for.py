lista = []

# Um simples exemplo de como podemos maninupular um for dentro de outro for
# Ou seja para cada valor de X vai aparecer 3X o valor de Y na tupla.
for x in range(3):
    for y in range(3):
        lista.append((x, y))

# print(lista)

# O mesmo exemplo acima usando list comprehension
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

# Agora eu gero uma nova list comprehension para cada valor de x.
lista = [
    [letra for letra in 'Luiz']
    for x in range(3)
]

print(lista)
