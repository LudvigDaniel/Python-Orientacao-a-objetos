

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite 
        
    def extrato(self):
        print("Saldo do titular Sr(a){} é de R${}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.saque(valor)
        destino.deposita(valor)

    def get_saldo(self):    
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    def get_limite(self):
        return self.__limite
    
    def get_conta(self):
        return self.__numero
    
    def set_limite(self, limite):
        self.__limite = limite

    