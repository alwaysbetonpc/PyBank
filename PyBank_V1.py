saldo = 0
limite = 500
extrato = ""   # ← string vazia
numero_de_saques = 0
LIMITE_SAQUE = 3

while True:
    print("\n" + "="*40)
    print(" MENU BANCO PYTHON ".center(40, "="))
    print("="*40)

    menu = input(("""
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Sair
    """).center(40) + "=> ")

  
    ###### DEPÓSITO #####
    if menu == "1":
        valor = float(input("Quanto quer depositar?: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido")

    ###### SAQUE ######
    if menu == "2":
        valor = float(input("Quanto você quer sacar?: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_de_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você não tem Saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido")

        elif valor > 0:
            saldo -= valor   # ← aqui era -= e não +=
            extrato += f"Saque: R${valor:.2f}\n"
            numero_de_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
    ###### EXTRATO ######
    elif menu == "3":
        print(" EXTRATO ".center(40, "#"))
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"Seu saldo atual é: R${saldo:.2f}".center(40))
        print("#" * 40)  # linha de fechamento
    ###### SAIR ######
    elif menu == "4":
        print("Obrigado por nos escolher como seu banco!")
        break
