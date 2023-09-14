def zipper(l1, l2):
    menor = l1 if len(l1) < len(l2) else l2
    # Uso range como forma de limitar respeitando a menor lista.
    return [(l2[i], l1[i]) for i in range(len(menor))]


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

result = zipper(l1, l2)
print(result)
