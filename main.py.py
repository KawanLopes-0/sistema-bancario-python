menu = """===== BANCO PYTHON =====\n\n1 - Depositar
2 - Sacar
3 - Consultar saldo
4 - Extrato
5 - Sair\n"""

def exibir_menu():
    print(menu)
    return int(input("Escolha uma opção: "))

selecao = exibir_menu()

deposito = 0
saque = 0
saldo = 0
extrato = []

while selecao != 5:

    if selecao == 1:
        print(f"===== DEPOSITAR =====\n")
        deposito = float(input(f"Digite o valor do depósito:\n"))
        
        if deposito <= 0:
            print(f"Não é possivel depositar valor negativo ou igual a zero\n")
        else:
            saldo += deposito
            extrato.append(f"Depósito: R$ +{deposito:.2f}")
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!\n")
        
    elif selecao == 2:
        print(f"===== SACAR =====\n")
        saque = float(input(f"Digite o valor do saque:\n"))
        
        if saque <= 0:
            print(f"Não é possivel sacar valor negativo ou igual a zero\n")
        elif saque > saldo:
            print(f"Saldo insuficiente para realizar o saque de R$ {saque:.2f}\n")
        else:
            saldo -= saque
            extrato.append(f"Saque: R$ -{saque:.2f}")
            print(f"Saque de R$ {saque:.2f} realizado com sucesso!\n")
        
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