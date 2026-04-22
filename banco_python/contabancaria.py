class ContaBancaria:
    """
    Classe que simula o comportamento de uma conta bancária.
    
    Atributos:
        _usuario (str): Nome do titular da conta.
        _saldo (float): Saldo disponível na conta.
    """
    def __init__(self, usuario, numero_conta,saldo=0, limite_valor_saque=500, limite_saque_por_dia=3,extrato=""):
        self._usuario = usuario
        self._numero_conta = numero_conta
        self._saldo = saldo
        self._limite_valor_saque = limite_valor_saque
        self._limite_saque_por_dia = limite_saque_por_dia
        self._extrato = extrato
    
    # Métodos Getter para acessar atributos privados
    def usuario(self):
        return self._usuario
    
    def numero_conta(self):
        return self._numero_conta
    
    def depositar(self, valor):
        """Adiciona um valor ao saldo da conta se o valor for positivo."""
        if valor > 0:
            self._saldo += valor
            self._extrato += f"Depósito: +{valor}\n"
        else:
            print("Valor inválido")
    
    def sacar(self, valor):
        """
        Realiza a retirada de dinheiro da conta.
        Verifica se há saldo suficiente, se o valor respeita o limite por saque
        e se o usuário ainda possui saques diários disponíveis.
        """
        if self._saldo >= valor and self._limite_valor_saque >= valor and self._limite_saque_por_dia > 0:
            self._saldo -= valor
            self._limite_saque_por_dia -= 1
            self._extrato += f"Saque: -{valor}\n"
        else:
            print("Saque não permitido")
            
    def extrato(self):
        """Retorna a string contendo o histórico de transações."""
        return self._extrato

def menu():
    """Retorna a representação visual do menu de opções."""
    menu = """
    Bem-vindo ao Banco Python
    
    1. Visualizar conta
    2. Depositar
    3. Sacar
    4. Extrato
    5. Sair
    """
    return menu

def criar_conta():
    """Solicita entradas do usuário para instanciar uma nova conta."""
    usuario = input("Digite o nome do titular da conta: ")
    numero_conta = input("Digite o número da conta: ")
    return ContaBancaria(usuario, numero_conta)

def main():
    """Função principal que gerencia o loop de interação com o usuário."""
    conta = criar_conta()
    while True:
        print(menu())
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            print(f"Titular: {conta.usuario()}\nNúmero da conta: {conta.numero_conta()}\nSaldo: {conta._saldo}")
        elif opcao == "2":
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
        elif opcao == "3":
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
        elif opcao == "4":
            print(conta.extrato())
        elif opcao == "5":
            print("Saindo...")
            break
main()
