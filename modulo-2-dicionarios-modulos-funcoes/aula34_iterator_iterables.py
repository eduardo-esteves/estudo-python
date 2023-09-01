import sys

iterable = [1, 2, 3, 4]
iterator = iter(iterable)

lista = [n for n in range(100000)]
generator_expr = (n for n in range(1, 1000000))

# Imprime o primeiro valor do iterable
print(iterator.__next__())
print()

# Imprime outuput: <class 'list_iterator'>
print(type(iterator))
print()

# Diferente da lista não imprime seus valores e sim o seu tipo e enderço em memória
# output: <generator object <genexpr> at 0x7f3091f46490>
print(generator_expr)
print()

# Aqui teremos o tamanho em bytes armazenado em memória
len_lista = sys.getsizeof(lista)
len_generator_expr = sys.getsizeof(generator_expr)

print(f'{len_lista=}, {len_generator_expr=}')

# Avanço três vezes a genexpr
generator_expr.__next__()
generator_expr.__next__()

print(generator_expr.__next__())
