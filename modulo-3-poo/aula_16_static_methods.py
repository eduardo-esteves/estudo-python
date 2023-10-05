from helper.print_msg_section import print_msg_section as print_msg
class Pessoa:
    num_pessoa = 0
    _count_pessoa = 0

    def __init__(self, idade):
        self.__idade = idade
        self.num_pessoa += 1
        # Isso torna a ideia de atributo estatico, atributo global pertencente a classe e não de uma instancia
        Pessoa._count_pessoa += 1

    def get_num_pessoa(self):
        return self.num_pessoa

    # Para tornar possível acessar
    def get_count_pessoa(self):
        return Pessoa._count_pessoa


eduardo = Pessoa(30)
qtd = eduardo.get_num_pessoa()

eduardo.num_pessoa += 1

print_msg('Total da var num_pessoa referente ao objeto "eduardo"')
print(qtd)

qtd = eduardo.get_num_pessoa()

print_msg('Note que contabiliza corretamente o valor de num_pessoa referente a instancia atual eduardo')
print(qtd)

# Como estou criando uma nova instancia de Pessoa o contador num_pessoa e reiniciado
marta = Pessoa(27)
joao = Pessoa(50)

print_msg('Note que num_pessoa é reiniciado devido ser uma nova instância de Pessoa')
print(marta.num_pessoa)

# Como quero saber o valor atual do atributo da classe, independente de suas instâncias em particular
print_msg('Total de pessoas com conceito de propriedade estatica')
print(Pessoa._count_pessoa)

# Note que ao pegar o valor atualizado de _count_pessoa com a instância eduardo
# não é uma atributo da instância eduardo e sim um atributo global da classe
# Pessoa seguindo o mesmo conceito de ser acessada via Pessoa._count_pessoa porém
# fazendo uso como se fosse um atributo local da instância eduardo.
edu_count = eduardo.get_count_pessoa()
print_msg('Acessando o valor atualizado global de _count_pessoa com a instância eduardo')
print(edu_count)
