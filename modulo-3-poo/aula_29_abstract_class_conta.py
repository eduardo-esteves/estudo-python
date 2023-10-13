from abc import ABC, abstractmethod

class Conta(ABC):

    _saldo = 0

    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta

        if saldo >= 0:
            self._saldo = saldo

    def get_info(self):
        return f"Agência: {self._agencia}, Conta: {self._conta}"

    def depositar(self, quantia):
        if quantia > 0:
            self._saldo += quantia

    def get_saldo(self):
        return self._saldo

    @abstractmethod
    def retirar(self, quantia):
        pass
