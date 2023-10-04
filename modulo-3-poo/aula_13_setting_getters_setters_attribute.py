class Televisao:
    def __init__(self, marca, ano, preco, n_canais):
        self.marca = marca
        self.__ano = ano
        self.__preco = preco
        self.n_canais = n_canais

    def aumentar_n_canais(self, qtd):
        self.n_canais += qtd

    # Metodo declado como private não posso acessar fora do escopo da classe.
    def __diminuir_n_canais(self, qtd):
        self.n_canais -= qtd

    def ponte_diminuir_canais(self, n_canais):
        self.__diminuir_n_canais(n_canais)

    @property
    def preco(self):
        return self.__preco

    # Para se ter um setter, devo ter obrigatoriamente um getter primeiro.
    @preco.setter
    def preco(self, n_preco):
        if not isinstance(n_preco, (int, float)):
            raise ValueError('O preço deve ser um numerico')

        if isinstance(n_preco, int):
            self.__preco = "{:.2f}".format(float(n_preco))
        else:
            self.__preco = "{:.2f}".format(n_preco)

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

    ano = property(fget=get_ano, fset=set_ano)

    def __str__(self):
        return f"Marca:{self.marca}, Ano:{self.__ano}, Preço:{self.__preco}, Números de Canais:{self.n_canais}"


t1 = Televisao('LG', 2023, 12.500, 120)

print(t1.ano)

t1.ano = 2032
print(t1.ano)



