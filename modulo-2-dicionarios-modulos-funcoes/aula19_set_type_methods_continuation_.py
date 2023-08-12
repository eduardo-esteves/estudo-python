# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Operadores úteis e metodos:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1.union(s2)

print(s3)
print()

# Intersecção
s4 = s1.intersection(s2)

print(s4)
print()

# Diferença entre dois conjuntos, em referência ao conjunto da esquerda que é s1
s5 = s1.difference(s2)

s6 = s1.symmetric_difference(s2)

print(s6)
