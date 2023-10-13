from abc import ABC, abstractmethod

# 57
class Conta(ABC):

    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta

        if saldo >= 0:
            self._saldo = saldo
        else:
            raise ValueError('O saldo não pode ser negativo')

    def get_info(self):
        return f"Agência: {self._agencia}, Conta: {self._conta}"

    def depositar(self, quantia):
        if quantia > 0:
            self._saldo += quantia
        else:
            raise ValueError('A quantia do depósito deve ser um valor positivo')

    def get_saldo(self):
        return self._saldo

    @abstractmethod
    def retirar(self, quantia):
        pass
