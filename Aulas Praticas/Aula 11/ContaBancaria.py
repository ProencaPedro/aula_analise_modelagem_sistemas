class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado.")
        
        else:
            print("Saldo Insuficiente!")

    def exibirSaldo(self):
        print(f"Saldo de {self.titular}: R${self.saldo: .2f}")


novaConta = ContaBancaria("Pedro", 500.00)
novaConta.depositar(200)
novaConta.exibirSaldo()
novaConta.sacar(700)
novaConta.exibirSaldo()