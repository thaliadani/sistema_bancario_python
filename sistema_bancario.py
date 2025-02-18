# Aqui é definido o menu do sistema bancário, que será exibido para o usuário.
# O menu é uma string multilinha (usando triple quotes) que contém as opções disponíveis.
menu = ("""
    ============= Bem vindo ao sistema bancário =============
    
        "Digite 1 para sacar"
        "Digite 2 para depositar"
        "Digite 3 para visualizar seu extrato"
        "Digite 4 para sair"
      """)

# Variável que armazena o saldo inicial do usuário, começando com R$ 0,00.
saldo = 0

# Variável que armazena o extrato das operações realizadas pelo usuário.
extrato = ""

# Define o valor máximo que pode ser sacado em uma única operação.
maximo_por_saque = 500

# Define o número máximo de saques que podem ser realizados em um dia.
LIMITE_DE_SAQUES = 3

# Inicia um loop infinito que só será interrompido quando o usuário escolher a opção de sair.
while True:
    # Exibe o menu e solicita que o usuário escolha uma opção.
    opcao = input(menu)
    
    # Verifica se a opção escolhida foi "1" (Sacar).
    if opcao == "1":
        print("Você escolheu sacar")
        
        # Solicita ao usuário o valor que deseja sacar.
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        
        # Verifica se o valor do saque é maior que o limite permitido por saque.
        if valor_saque > maximo_por_saque:
            print("O valor máximo por saque é de R$500,00")
        
        # Verifica se o usuário já atingiu o limite de saques diários.
        elif LIMITE_DE_SAQUES == 0:
            print("Você atingiu o limite de saques diários")
        
        # Caso todas as verificações sejam atendidas, o saque é realizado.
        else:
            # Decrementa o limite de saques disponíveis.
            LIMITE_DE_SAQUES -= 1
            
            # Subtrai o valor do saque do saldo.
            saldo -= valor_saque
            
            # Adiciona a operação de saque ao extrato.
            extrato += f"Saque: R${valor_saque:.2f}\n"
    
    # Verifica se a opção escolhida foi "2" (Depositar).
    elif opcao == "2":
        print("Você escolheu depositar")
        
        # Solicita ao usuário o valor que deseja depositar.
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        
        # Adiciona o valor do depósito ao saldo.
        saldo += valor_deposito
        
        # Adiciona a operação de depósito ao extrato.
        extrato += f"Depósito: R${valor_deposito:.2f}\n"
    
    # Verifica se a opção escolhida foi "3" (Visualizar extrato).
    elif opcao == "3":
        print("Você escolheu visualizar seu extrato")
        
        # Exibe o extrato das operações realizadas.
        print(extrato)
    
    # Verifica se a opção escolhida foi "4" (Sair).
    elif opcao == "4":
        print("Você escolheu sair")
        
        # Interrompe o loop e encerra o programa.
        break
    
    # Caso o usuário digite uma opção inválida, exibe uma mensagem de erro.
    else:
        print("Opção inválida, tente novamente")