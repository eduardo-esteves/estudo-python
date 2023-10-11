from helper.print_msg_section import print_msg_section as print_msg

# 46
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


eduardo = Gerente('Eduardo', '22222222', 10000, '1232', 4)
monica = Secretaria('Monica', '111111111', 9000, 2)
gestao = GestaoBonus

print_msg('Instancia de Eduardo')
print(eduardo)
gestao.registrar_bonus(eduardo)

print_msg('Instancia de Monica')
print(monica)
gestao.registrar_bonus(monica)

print_msg('Total de bonus secretaria:1800 + gerente:4000')
total_bonificacao = gestao.show_total_bonus()
print(total_bonificacao)
