class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class ContaBancaria:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def obter_extrato(self):
        print(f"Saldo atual: R${self.saldo}")

def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    cpf = input("CPF do cliente: ")
    return Cliente(nome, cpf)

def cadastrar_conta_bancaria(cliente):
    return ContaBancaria(cliente)

# Cadastrar cliente
cliente = cadastrar_cliente()

# Cadastrar conta bancária
conta = cadastrar_conta_bancaria(cliente)

# Exemplo de uso da conta bancária
conta.depositar(100)
conta.obter_extrato()
conta.sacar(50)
conta.obter_extrato()
