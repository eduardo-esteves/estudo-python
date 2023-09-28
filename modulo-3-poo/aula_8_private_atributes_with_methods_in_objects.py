class Televisao_3:
    def __init__(self, marca, ano, preco, n_canais):
        self.marca = marca
        # Torno ano um atributo private, ou seja não será mais visivel este atributo em sua manipulação.
        self.__ano = ano
        self.preco = preco
        self.n_canais = n_canais

    def update_ano(self, ano: int):
        self.__ano = ano

    def __str__(self):
        return f"Marca:{self.marca}, Ano:{self.__ano}, Preço:{self.preco}, Números de Canais:{self.n_canais}"


t1 = Televisao_3('LG', 2023, 12.500, 120)

# A pesar de ser um atributo private estou conseguindo modificar diretamente seu valor o que
# não é comum em outras linguagens de programação com suporte a OOP.
t1.ano = 2025
print(t1)

# Torno possível a atualização do atributo privado __ano através de metódos públicos
t1.update_ano(2026)
print(t1)
