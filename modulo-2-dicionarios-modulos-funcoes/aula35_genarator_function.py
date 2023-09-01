# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n

        if n >= maximum:
            return

        n += 1

def gen_function(n=0):
    # Pausa a execução
    yield 1
    return 'Executou'


gen = gen_function(0)
print(next(gen))
# gen = generator(maximum=1000000)
# for n in gen:
#     print(n)
