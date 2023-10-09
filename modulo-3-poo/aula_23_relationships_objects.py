from helper.print_msg_section import print_msg_section as print_msg

# 40
# Um exemplo de como as classes podem ter atributos e métodos que se
# relacionam entre si, Funcionario extends Pessoa
class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

# Um gerente também é um funcionario então para não haver repetição
# de código poderiamos ter usado o conceito de herança onde um
# Gerente extends Funcionario
class Gerente:
    def __init__(self, nome, cpf, salario, senha, qtd_subordinados):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._senha = senha
        self._qtd_subordinados = qtd_subordinados

# Uma secretária extends Funcionario
class Secretaria:
    def __init__(self, nome, cpf, salario, senha, qtd_gerentes):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._senha = senha
        self._qtd_gerentes = qtd_gerentes
