from helper.print_msg_section import print_msg_section as print_msg

# 34
class Pessoa:
    num_pessoa = 0
    _count_pessoa = 0

    def __init__(self, nome, idade):
        self.nome = nome
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

    # Aqui temos um safe guardian para manipular um exemplo de slots, note que a
    # propriedade sexo não faz parte do escopo da classe, e só terá valor caso o
    # usuário atribuir essa propriedade dinamicamente na instancia de um objeto
    # do tipo Pessoa
    def __str__(self):
        sexo = None
        if (hasattr(self, 'sexo')):
            sexo = self.sexo

        return f"{self.nome=}, {self.__idade=}, {sexo=},  {self.num_pessoa=}, {self._count_pessoa=}"



eduardo = Pessoa('Eduardo', 30)
maria = Pessoa('Maria', 50)

# Atribuindo um atributo dinâmico que ainda não existe nas instâncias eduardo e maria
# e ao debugarmos o novo atributo passa a existir
# ['_Pessoa__idade', '__class__', '__dict__', '__dir__', '__doc__', 'get_num_pessoa', 'nome', 'num_pessoa', 'sexo']
eduardo.sexo = 'M'
maria.sexo = 'F'

print_msg('Propriedades e seus valores da instancia eduardo')
print(eduardo)
