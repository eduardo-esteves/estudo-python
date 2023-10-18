from aula_30_class_conta_poupanca import ContaPoupanca


conta_poupanca = ContaPoupanca('3182', '4554555', -12222)

if not conta_poupanca.retirar(10000):
    print('Você não tem saldo suficiente para sacar')

saldo = conta_poupanca.get_saldo()

print(saldo)
