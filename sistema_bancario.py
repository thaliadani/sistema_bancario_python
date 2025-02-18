menu= ("""
    ============= Bem vindo ao sistema bancário =============
    
        "Digite 1 para sacar"
        "Digite 2 para depositar"
        "Digite 3 para visualizar seu extrato"
        "Digite 4 para sair"
      """)

saldo = 0
extrato = ""
maximo_por_saque =  500
LIMITE_DE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "1":
        print("Você escolheu sacar")
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        if valor_saque > maximo_por_saque:  
            print("O valor máximo por saque é de R$500,00")
        elif LIMITE_DE_SAQUES == 0:
            print("Você atingiu o limite de saques diários")
        else:
            LIMITE_DE_SAQUES -= 1
            saldo -= valor_saque
            extrato += f"Saque: R${valor_saque:.2f}\n"
    elif opcao == "2":
        print("Você escolheu depositar")
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        saldo += valor_deposito
        extrato += f"Depósito: R${valor_deposito:.2f}\n"   
    elif opcao == "3":
        print("Você escolheu visualizar seu extrato")
        print(extrato)
    elif opcao == "4":
        print("Você escolheu sair")
        break
    else:
        print("Opção inválida, tente novamente")
        