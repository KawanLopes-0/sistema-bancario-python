menu = """===== BANCO PYTHON =====\n\n1 - Depositar
2 - Sacar
3 - Consultar saldo
4 - Extrato
5 - Sair\n"""

def exibir_menu():
    print(menu)
    while True:
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Por favor, escolha uma opção válida.\n")
            print(menu)

def depositar(valor, saldo, extrato):

    if valor <= 0:
        print(f"Não é possivel depositar valor negativo ou igual a zero\n")
    else:
        saldo += valor
        extrato.append(f"Depósito: R$ +{valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!\n")
    return saldo

def sacar(saque, saldo, extrato):
    if saque <= 0:
        print(f"Não é possivel sacar valor negativo ou igual a zero\n")
    elif saque > saldo:
        print(f"Saldo insuficiente para realizar o saque de R$ {saque:.2f}\n")
    else:
        saldo -= saque
        extrato.append(f"Saque: R$ -{saque:.2f}")
        print(f"Saque de R$ {saque:.2f} realizado com sucesso!\n")
    return saldo

selecao = exibir_menu()
saldo = 0
extrato = []

while selecao != 5:

    if selecao == 1:
        print(f"===== DEPOSITAR =====\n")

        while True:
            try:
             valor = float(input(f"Digite o valor do depósito:\n"))
             break
            except ValueError:
             print("\nValor inválido.\n")

        saldo = depositar(valor, saldo, extrato)

    elif selecao == 2:
        print(f"===== SACAR =====\n")
        
        while True:
         try:
          saque = float(input(f"Digite o valor do saque:\n"))
          break
         except ValueError:
          print("\nValor inválido.\n")

        saldo = sacar(saque, saldo, extrato)
        
    elif selecao == 3:
        print(f"===== CONSULTAR SALDO =====\n")
        print(f"Seu saldo atual é: R$ {saldo:.2f}\n")
        
    elif selecao == 4:
        print(f"===== EXTRATO =====\n")
        if not extrato:
            print("Não há movimentações no extrato.\n")
        else:
            for movimento in extrato:
                print(movimento)

    else:
        print("Opção inválida.\n")

    selecao = exibir_menu()

print("Obrigado por utilizar o Banco Python. Até logo!")