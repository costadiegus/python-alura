class Conta:
    def __init__(self, numero: int, titular: str, saldo: float, limite: float = 1000.0):
        print("Construindo algo...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo {self.saldo} do titular {self.titular}")
        print(f"Conta nº {self.numero} com limte de {self.limite}")

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
