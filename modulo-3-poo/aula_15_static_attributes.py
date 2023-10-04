class Pessoa:
    num_pessoa = 0
    count_pessoa = 0

    def __init__(self, idade):
        self.__idade = idade
        self.num_pessoa += 1
        # Isso torna a ideia de atributo estatico, atributo global pertencente a classe e não de uma instancia
        Pessoa.count_pessoa += 1

    def get_num_pessoa(self):
        return self.num_pessoa


eduardo = Pessoa(30)
qtd = eduardo.get_num_pessoa()

eduardo.num_pessoa += 1

print(qtd)

qtd = eduardo.get_num_pessoa()

print(f'Contabiliza corretamente somente na instancia atual eduardo {qtd}')

# Como estou criando uma nova instancia de Pessoa o contador num_pessoa e reiniciado
marta = Pessoa(27)
print(marta.num_pessoa)

# Como quero saber o valor atual do atributo da classe, independente de suas instâncias em particular
print(f'Total de pessoas é: {Pessoa.count_pessoa}')
