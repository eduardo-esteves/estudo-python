from helper.print_msg_section import print_msg_section as print_msg

# 37
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


# Criando uma nova instância via metodos magicos do objeto Pessoa
eduardo = object.__new__(Pessoa)
eduardo.__init__('Eduardo', 30)

print(eduardo)
