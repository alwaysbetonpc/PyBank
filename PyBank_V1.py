menu = """
================ MENU ================
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
======================================
=> """

saldo = 0
limite = 500
extrato = ""   # string vazia
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    # Depósito
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Saque
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_de_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Extrato
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato, end="")  # mostra cada depósito e saque registrado
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # Sair
    elif opcao == "4":
        print("Saindo do sistema... Obrigado por usar nosso banco!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
