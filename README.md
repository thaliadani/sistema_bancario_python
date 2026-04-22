# Sistema Bancário Python

Este é um projeto simples em Python que simula as operações básicas de um sistema bancário, como depósitos, saques e visualização de extrato. Ele foi desenvolvido como uma biblioteca para fins educacionais e de prática da linguagem Python.

## 🚀 Funcionalidades

- **Criação de Conta:** Permite registrar um titular e um número de conta.
- **Depósitos:** Adiciona valores ao saldo da conta.
- **Saques:** Permite retirar dinheiro respeitando limites de valor por saque e quantidade de saques diários.
- **Extrato:** Exibe o histórico de transações realizadas.
- **Interface CLI:** Menu interativo para facilitar a navegação do usuário.

## 🛠️ Tecnologias Utilizadas

- [Python 3.6+](https://www.python.org/)

## 📦 Instalação

Para instalar as dependências necessárias (caso existam futuramente) e configurar o pacote, você pode usar:

```bash
pip install .
```

## 💻 Como Usar

Para iniciar o sistema e interagir com o menu, basta executar o arquivo principal:

```bash
python banco_python/contabancaria.py
```

### Exemplo de Uso (Código)

Você também pode importar a classe `ContaBancaria` em seus próprios scripts:

```python
from banco_python.contabancaria import ContaBancaria

conta = ContaBancaria("Thalia", "12345-6")
conta.depositar(1000)
conta.sacar(200)
print(conta.extrato())
```

## 👤 Autor

* **Thalia Danielle** - thalia.dani2@gmail.com

## 📄 Licença

Este projeto está sob a licença MIT - consulte o arquivo LICENSE para detalhes.