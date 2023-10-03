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

# Um truque para acessar e modificar valores de atributos privados
atributo_privado = t1._Televisao_3__ano = 2024
print(atributo_privado)
