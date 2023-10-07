from helper.print_msg_section import print_msg_section as print_msg

# 35,36
class Pessoa:
    _count_pessoa = 0
    __slots__ = ['nome', '__idade']

    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade
        # Isso torna a ideia de atributo estatico, atributo global pertencente a classe e não de uma instancia
        Pessoa._count_pessoa += 1

    # Para tornar possível acessar via isntância da classe, e tirando a obrigatoriedade de
    # atribuir o argumento obrigatório self na declaração de métodos
    @staticmethod
    def get_count_pessoa():
        return Pessoa._count_pessoa

    # Note que essa condição safe guard é totalmente desnecessária já que caso o
    # usuário não respeite o contrato da classe e tente atribuir qualquer atributo
    # que não existe na definição do construtor será lançado um AttributeError:
    # informando que tal atributo não existe no objeto Pessoa e nem chega nessa condição.
    def __str__(self):
        sexo = None

        if (hasattr(self, 'sexo')):
            sexo = self.sexo

        return f"{self.nome=}, {self.__idade=}, {sexo=}, {self._count_pessoa=}"



eduardo = Pessoa('Eduardo', 30)
maria = Pessoa('Maria', 50)

# Atribuindo um atributo dinâmico que ainda não existe nas instâncias eduardo e maria
# e ao debugarmos o novo atributo passa a existir
# ['_Pessoa__idade', '__class__', '__dict__', '__dir__', '__doc__', 'get_num_pessoa', 'nome', 'num_pessoa', 'sexo']
#eduardo.sexo = 'M'
#maria.sexo = 'F'

# Note que a partir do momento em que implemento slots perco a propriedade
# __dict__ dentro do objeto e com isso não permite mais atribuição dinamica
# e também a listagem das propriedades declarada a nivel de classe vars(obj)
print_msg('Não tem mais a propriedade __dict__ na instancia eduardo após implementar __slots__')
print(dir(eduardo))
