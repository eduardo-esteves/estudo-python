from helper.print_msg_section import print_msg_section as print_msg

# 41, 42

class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def __str__(self):
        return f"{self._nome=}, {self._cpf=}, {self._salario=}"

# Note que em Python não preciso declarar extends Funcionario como em outras linguagens
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_subordinados):
        # Aqui estou chamando o constructor sem o uso de super()
        Funcionario.__init__(self, nome, cpf, salario)
        self._senha = senha
        self._qtd_subordinados = qtd_subordinados

    def __str__(self):
        return f"{self._nome=}, {self._cpf=}, {self._salario=}, {self._senha=}, {self._qtd_subordinados=}"

class Secretaria(Funcionario):
    def __init__(self, nome, cpf, salario, qtd_gerentes):
        # Aqui como estou usando super não devo passar self no constructor
        # isso porque self estaria se referindo a instância de Secretaria.
        super().__init__(nome, cpf, salario)
        self._qtd_gerentes = qtd_gerentes

    def __str__(self):
        return f"{self._nome=}, {self._cpf=}, {self._salario=}, {self._qtd_gerentes=}"


eduardo = Gerente('Eduardo', '22222222', 10.000,'1232', 4)
monica = Secretaria('Monica', '111111111', 9.000, 2)

print_msg('Instancia de Eduardo')
print(eduardo)

print_msg('Instancia de Monica')
print(monica)
