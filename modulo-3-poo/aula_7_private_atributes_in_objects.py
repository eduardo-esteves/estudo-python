class Televisao_3:
    def __init__(self, marca, ano, preco, n_canais):
        self.marca = marca
        # Torno ano um atributo private, ou seja não será mais visivel e não será mais possível
        # modificar o valor deste atributo fora da classe.
        self.__ano = ano
        self.preco = preco
        self.n_canais = n_canais

    def __str__(self):
        return f"Marca:{self.marca}, Ano:{self.__ano}, Preço:{self.preco}, Números de Canais:{self.n_canais}"


t1 = Televisao_3('LG', 2023, 12.500, 120)
# Por ser um atributo do tipo private não consigo mais modificar diretamente seu valor tornando
# o mesmo  comportamento comum em outras linguagens de programação com suporte a OOP.
t1.__ano = 2025

print(t1)
