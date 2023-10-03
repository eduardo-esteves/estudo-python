class Televisao:
    def __init__(self, marca, ano, preco, n_canais):
        self.marca = marca
        self.ano = ano
        self.preco = preco
        self.n_canais = n_canais

    def aumentar_n_canais(self, qtd):
        self.n_canais += qtd


    # Metodo declado como private não posso acessar fora do escopo da classe.
    def __diminuir_n_canais(self, qtd):
        self.n_canais -= qtd


    def ponte_diminuir_canais(self, n_canais):
        self.__diminuir_n_canais(n_canais)


    def __str__(self):
        return f"Marca:{self.marca}, Ano:{self.ano}, Preço:{self.preco}, Números de Canais:{self.n_canais}"


t1 = Televisao('LG', 2023, 12.500, 120)
t1.aumentar_n_canais(20)
# Uma excessão do tipo AttributeError será lançada caso eu tente acessar
# t1.__diminuir_n_canais(10) devido ser private e não pode ser acessada fora da classe.

# Estou usando uma função do tipo public para servir de ponte e atualizar
# o número de canais chamando o método private
t1.ponte_diminuir_canais(10)
print(t1)

