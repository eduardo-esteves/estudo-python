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

    # Para tornar possível acessar via isntância da classe, e tirando a obrigatoriedade de
    # atribuir o argumento obrigatório self na declaração de métodos
    @staticmethod
    def get_count_pessoa():
        return Pessoa._count_pessoa


eduardo = Pessoa(30)
joao = Pessoa(50)
# Note que não houve mudança na chamada via instância, somente na declaração da função
# e com o decorator não preciso mais da palavra chave self como argumento, e fica acessivel
# também via objeto global da classe Pessoa, ver abaixo linha 33
qtd = eduardo.get_count_pessoa()

print_msg('Acesso da propriedade estatica Via instancia de classe')
print(qtd)

# Total de pessoas com conceito de propriedade estatica via objeto global da classe
qtd_static = Pessoa.get_count_pessoa()

print_msg('Acesso da propriedade estatica via objeto global da classe')
print(qtd_static)
