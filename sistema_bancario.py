class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.maximo_por_saque = 500
        self.limite_de_saques = 3
        self.extrato = ""
    
    def criar_usuario(self):
        nome = input("Digite o seu nome: ")
        return nome

    def criar_conta_corrente(self):
        numero_da_conta = input("Digite o número da conta: ")
        return numero_da_conta
   
    def sacar(self):
        if self.limite_de_saques == 0:
            print("Você atingiu o limite de saques diários.")
            return

        valor_saque = float(input("Digite o valor que deseja sacar: "))

        if valor_saque > self.maximo_por_saque:
            print("O valor máximo por saque é de R$500,00.")
        elif valor_saque > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor_saque
            self.limite_de_saques -= 1
            self.extrato += f"Saque: R${valor_saque:.2f}\n"
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")

    def depositar(self):
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        self.saldo += valor_deposito
        self.extrato += f"Depósito: R${valor_deposito:.2f}\n"
        print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")

    def visualizar_extrato(self):
        print("\n========== EXTRATO ==========")
        print("Movimentações:")
        print(self.extrato if self.extrato else "Não foram realizadas movimentações.")
        print(f"Saldo atual: R${self.saldo:.2f}")
        print("=============================")


def main():
    conta = ContaBancaria()
    usuario = None
    numero_conta = None
    ERRO_USUARIO_CONTA = "Você precisa criar um usuário e uma conta corrente primeiro."

    while True:
        menu = """
        ============ Bem-vindo ao sistema bancário ============
        
        Digite 1 para criar usuário
        Digite 2 para criar conta corrente
        Digite 3 para sacar
        Digite 4 para depositar
        Digite 5 para visualizar seu extrato
        Digite 6 para sair
        """
        
        opcao = input(menu)
        
        if opcao == "1":
            usuario = conta.criar_usuario()
            print(f"Usuário criado com sucesso: {usuario}")
        
        elif opcao == "2":
            numero_conta = conta.criar_conta_corrente()
            print(f"Conta corrente criada com sucesso: {numero_conta}")
        
        elif opcao == "3":
            if usuario and numero_conta:
                conta.sacar()
            else:
                print(ERRO_USUARIO_CONTA)
        
        elif opcao == "4":
            if usuario and numero_conta:
                conta.depositar()
            else:
                print(ERRO_USUARIO_CONTA)
        
        elif opcao == "5":
            if usuario and numero_conta:
                conta.visualizar_extrato()
            else:
                print(ERRO_USUARIO_CONTA)
        
        elif opcao == "6":
            print("Obrigado por usar nosso sistema bancário.")
            break
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()