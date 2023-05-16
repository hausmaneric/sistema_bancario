class ContaBancaria:
    def __init__(self, nome_cliente):
        self.nome_cliente = nome_cliente
        self.saldo = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +{valor}")
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: -{valor}")
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def visualizar_extrato(self):
        print("Extrato:")
        for operacao in self.extrato:
            print(operacao)
        print(f"Saldo atual: {self.saldo}")


# Exemplo de uso
conta = ContaBancaria("João")

conta.depositar(100)
conta.sacar(50)
conta.visualizar_extrato()
