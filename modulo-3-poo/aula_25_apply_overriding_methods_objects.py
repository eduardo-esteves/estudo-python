from helper.print_msg_section import print_msg_section as print_msg

# 44

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


eduardo = Gerente('Eduardo', '22222222', 10000,'1232', 4)
monica = Secretaria('Monica', '111111111', 9000, 2)

print_msg('Instancia de Eduardo')
print(eduardo)
salario_eduardo = eduardo._salario
salario_eduardo_bonus = salario_eduardo + eduardo.bonus_dez_p_cento()
print(salario_eduardo_bonus)


print_msg('Instancia de Monica')
print(monica)
salario_monica = monica._salario
salario_monica_bonus = salario_monica + monica.bonus_dez_p_cento()

print(salario_monica_bonus)

