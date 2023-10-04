class Televisao:
    def __init__(self, marca, ano):
        self.marca = marca
        self.__ano = ano
        self._modelo = 'Mitia'


    def _info_televisao(self):
        print(f'A marca é {self.marca} ano {self.__ano} e modelo {self._modelo} ')


    def __str__(self):
        return f"Marca:{self.marca}, Ano:{self.__ano}"


t1 = Televisao('LG', 2023)

print(t1.marca)
# Macete para acessar um atributo mesmo que seja privado
print(t1._Televisao__ano)
# Imprimir métodos e atributos de um objeto
print(dir(t1))

# Embora _modelo tenha a ideia de protected isso é apenas uma convensão e não um encapsulamento
print(t1._modelo)


info = t1._info_televisao()

# Um metodo que não tem um retorno sempre retorna None por padrão
print(info)

