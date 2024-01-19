from datetime import datetime

class Usuario:
    def __init__(self, conta_corrente, senha):
        self.conta_corrente = conta_corrente
        self.senha = senha
        self.saldo = 0
        self.transacoes = []
        self.saques_realizados = 0

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso. Novo saldo: R${self.saldo}")
        else:
            print("Valor de depósito inválido.")

    def saque(self, valor):
        if valor > 0 and valor <= 500 and self.saques_realizados < 3:
            self.saldo -= valor
            self.saques_realizados += 1
            self.transacoes.append(f'Saque de R${valor} em {datetime.now()}')
            print(f'Saque de R${valor} realizado. Saldo atual: R${self.saldo}')
        elif valor > 500:
            print('Limite máximo por saque é de R$500.')
        elif self.saldo < valor:
            print('Saldo insuficiente para realizar o saque.')
        elif self.saques_realizados >= 3:
            print('Você atingiu o limite máximo de saques por dia.')
        else:
            print("Valor de saque inválido.")    

    def extrato(self):
       print(f'\nExtrato:')
       print(f'Número da conta: {self.conta_corrente}')
       print(f'Saldo atual: R${self.saldo}')
       print(f'Saques realizados hoje: {self.saques_realizados}')
       print('\nTransações realizadas hoje:')
       for transacao in self.transacoes:
            print(transacao)

def login():
    conta_corrente = input("Digite o número da conta corrente: ")
    senha = input("Digite a senha: ")
    return conta_corrente, senha

def menu_principal(usuario):
    while True:
        print("\nOpções:")
        print("1. Saque")
        print("2. Depósito")
        print("3. Extrato")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_saque(usuario)
        elif opcao == "2":
            menu_deposito(usuario)
        elif opcao == "3":
            usuario.extrato()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_saque(usuario):
    while True:
        valor = float(input("Digite o valor do saque (máximo R$500): "))
        usuario.saque(valor)
        sair = input("Deseja sair? (s/n): ")
        if sair.lower() == "s":
            break

def menu_deposito(usuario):
    while True:
        valor = float(input("Digite o valor do depósito: "))
        usuario.deposito(valor)
        sair = input("Deseja sair? (s/n): ")
        if sair.lower() == "s":
            break

if __name__ == "__main__":
    usuarios = {"123456": "senha123", "789012": "senha456"}  
    conta_corrente, senha = login()

    if conta_corrente in usuarios and usuarios[conta_corrente] == senha:
        usuario_atual = Usuario(conta_corrente, senha)
        menu_principal(usuario_atual)
    else:
        print("Credenciais inválidas.")
