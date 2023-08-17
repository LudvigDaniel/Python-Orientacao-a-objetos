

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

    def pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saque(self, valor):
        if(self.pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Saque Recusado. O Valor R${} ultrapassa o limite. Entre em contato com o seu Gerente" .format(valor))

    def transferir(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def get_saldo(self):
        return self.__saldo
    
    @property
    def get_titular(self):
        return self.__titular, self.__numero
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

