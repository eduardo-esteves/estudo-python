from helper.print_msg_section import print_msg_section as print_msg

# 50
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


class ClubeGerentes:

    def __init__(self, clube, funcionarios):
        self._clube = clube
        self._funcionarios = funcionarios

    def listar_funcionarios(self):
        return self._funcionarios

    def __getitem__(self, item):
        return self._funcionarios[item]

    # A partir de agora o objeto ClubeGerentes possui também o método mágico __len__ e passa a
    # se comportar de maneira diferente antes de atribuirmos esse método magico podendo usar len(self)
    def __len__(self):
        return len(self._funcionarios)

    def total_socios(self):
        return len(self._funcionarios)


eduardo = Gerente('Eduardo', '22222222', 10000, '1232', 4)
marcela = Gerente('Marcela', '11111111', 7000, '1232', 4)
vitor = Gerente('Vitor', '333333333', 12000, '1232', 4)


lista_gerentes = [eduardo, marcela, vitor]


clubes = ClubeGerentes('Maior Legal', lista_gerentes)

lista_socios = clubes.listar_funcionarios()
total_socios = clubes.total_socios()

print_msg('Lista de Socios')
print(lista_socios)

print_msg('Total de Socios')
print(total_socios)

len(clubes)
