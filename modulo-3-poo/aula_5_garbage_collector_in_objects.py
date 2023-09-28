import gc


class Televisao_4:
    def __init__(self, marca, ano, preco, n_canais):
        self.marca = marca
        self.ano = ano
        self.preco = preco
        self.n_canais = n_canais

    def aumentar_n_canais(self, qtd):
        self.n_canais += qtd

    def diminuir_n_canais(self, qtd):
        self.n_canais -= qtd

    def __str__(self):
        return f"Marca:{self.marca}, Ano:{self.ano}, Preço:{self.preco}, Números de Canais:{self.n_canais}"


# Entendo como funciona o Garbage collector no Python, a partir do momento que instanciamos um objeto
t1 = Televisao_4('LG', 2023, 12.500, 120)
# Temos um endereço único desse objeto na memória
endereco_memoria_t1 = id(t1)

# A partir do momento que crio uma nova instância daquele objeto e atribuo seu valor para um objeto
# já existente que coincidentemente ou não tenha uma referência em memória de uma outra intância qualquer
# do mesmo objeto, ou outro objeto o Garbage Collector faz a limpeza em memória daquele endereço alocado
# para esse objeto e realoca um novo endereço.
t1 = Televisao_4('LG', 2023, 12.500, 120)
endereco_memoria_t2 = id(t1)

print(t1)
print()

print(f"{endereco_memoria_t1=}")
print(f"{endereco_memoria_t2=}")

"""
Output:
endereco_memoria_t1=140387567174288
endereco_memoria_t2=140387567174352
"""

t2 = Televisao_4('LG', 2023, 12.500, 120)
t3 = Televisao_4('LG', 2023, 12.500, 120)


# Deleto a referência de t2 e t3, note que se trata de gerenciamento de memória
del t2
del t3

# Run garbage collection manually
gc.collect()

print(f"{t2=}, {t3=}")
