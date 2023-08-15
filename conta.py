

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite 
        
    def extrato(self):
        print("Saldo do titular Sr(a){} é de R${}".format(self.titular, self.saldo))

    def deposita(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor


        
