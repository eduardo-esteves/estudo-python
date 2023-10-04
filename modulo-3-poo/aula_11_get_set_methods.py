class Televisao:
    def __init__(self, marca, ano, preco, n_canais):
        self.marca = marca
        self.__ano = ano
        self.preco = preco
        self.n_canais = n_canais

    def aumentar_n_canais(self, qtd):
        self.n_canais += qtd

    # Metodo declado como private não posso acessar fora do escopo da classe.
    def __diminuir_n_canais(self, qtd):
        self.n_canais -= qtd

    def ponte_diminuir_canais(self, n_canais):
        self.__diminuir_n_canais(n_canais)

    def set_ano(self, ano):
        if isinstance(ano, int):
            try:
                ano = int(ano) if ano > 2000 else self.get_ano()
            except Exception:
                print('Por favor forneça um ano válido')
                return

        self.__ano = ano

    def get_ano(self):
        return self.__ano

    def __str__(self):
        return f"Marca:{self.marca}, Ano:{self.ano}, Preço:{self.preco}, Números de Canais:{self.n_canais}"


t1 = Televisao('LG', 2023, 12.500, 120)

t1.set_ano(False)
ano = t1.get_ano()

print(ano)
