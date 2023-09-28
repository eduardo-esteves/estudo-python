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


t1 = Televisao_4('LG', 2023, 12.500, 120)
t1.aumentar_n_canais(20)

print(t1)

