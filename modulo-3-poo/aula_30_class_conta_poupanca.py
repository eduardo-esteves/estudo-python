from aula_29_abstract_class_conta import Conta


class ContaPoupanca(Conta):

    def __init__(self, agencia, conta, saldo):
        super().__init__(agencia, conta, saldo)
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    def retirar(self, quantia):
        if self._saldo >= quantia:
            self._saldo -= quantia
        else:
            return False
        return True
