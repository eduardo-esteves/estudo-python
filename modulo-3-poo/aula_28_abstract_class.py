from collections.abc import MutableSequence

from helper.print_msg_section import print_msg_section as print_msg

# 56
class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def bonus_dez_p_cento(self):
        return self._salario * 0.10

    def __str__(self):
        return f"{self._nome=}, {self._cpf=}, {self._salario=}"


# Note que em Python não preciso declarar extends Funcionario como em outras linguagens
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_subordinados):
        # Aqui estou chamando o constructor sem o uso de super()
        Funcionario.__init__(self, nome, cpf, salario)
        self._senha = senha
        self._qtd_subordinados = qtd_subordinados

    # Sobrescrita método Funcionario
    def bonus_dez_p_cento(self):
        return self._salario * (0.10 * self._qtd_subordinados)

    def __str__(self):
        return f"{self._nome=}, {self._cpf=}, {self._salario=}, {self._senha=}, {self._qtd_subordinados=}"


class Secretaria(Funcionario):
    def __init__(self, nome, cpf, salario, qtd_gerentes):
        # Aqui como estou usando super não devo passar self no constructor
        # isso porque self estaria se referindo a instância de Secretaria.
        super().__init__(nome, cpf, salario)
        self._qtd_gerentes = qtd_gerentes

    # Sobrescrita método Funcionario
    def bonus_dez_p_cento(self):
        return self._salario * (0.10 * self._qtd_gerentes)

    def __str__(self):
        return f"{self._nome=}, {self._cpf=}, {self._salario=}, {self._qtd_gerentes=}"


class GestaoBonus:

    __total_bonus = 0

    # Aqui acontece o polimorfismo exatamente quando cada classe chamar
    # seu próprio método bonus_dez_p_cento() eles devem receber os mesmos
    # atributos e retornar o mesmo tipo de dado por convensão.
    def registrar_bonus(funcionario):
        GestaoBonus.__total_bonus += funcionario.bonus_dez_p_cento()

    @staticmethod
    def show_total_bonus():
        return GestaoBonus.__total_bonus


class ClubeGerentes(MutableSequence):

    _funcionarios = []

    def __init__(self, clube, funcionarios):
        self._clube = clube
        self._funcionarios = funcionarios

    def listar_funcionarios(self):
        return self._funcionarios

    def __delitem__(self, key):
        del self._funcionarios[key]

    def __getitem__(self, item):
        return self._funcionarios[item]

    def __len__(self):
        return len(self._funcionarios)

    def __setitem__(self, key, value):
        self._funcionarios[key] = value

    def insert(self, index, value):
        # Insere o novo elemento na posição especificada
        self._funcionarios.insert(index, value)


eduardo = Gerente('Eduardo', '22222222', 10000, '1232', 4)
marcela = Gerente('Marcela', '11111111', 7000, '1232', 4)
vitor = Gerente('Vitor', '333333333', 12000, '1232', 4)


lista_gerentes = [eduardo, marcela, vitor]

cg = ClubeGerentes('São Paulo', lista_gerentes)
segundo_elem = cg[1]
todos_func = cg.listar_funcionarios()

novo_gerente = Gerente('Novo Gerente', '44444444', 9500, '1234', 3)
posicao = len(cg)
cg.insert(posicao, novo_gerente)
# Gerando uma lista de gerentes do tipo dict, sendo possível manipular como uma lista de dicionarios
#lista_funcionarios = cg.listar_funcionarios()
lista_funcionarios = [gerente.__dict__ for gerente in cg.listar_funcionarios()]


print_msg('__getitem__')
print(segundo_elem)

print_msg('listar_funcionarios()')
print(lista_funcionarios)
