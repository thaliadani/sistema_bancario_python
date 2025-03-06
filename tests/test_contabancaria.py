from banco_python.contabancaria import ContaBancaria

conta = ContaBancaria("", "")
conta.depositar(100)
conta.sacar(50)
print(conta.extrato())