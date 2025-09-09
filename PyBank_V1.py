import textwrap

# ------------------- MENU -------------------
def exibir_menu():
    menu = """
================ BANCO PY ================
[1] Depositar Dinheiro
[2] Sacar Dinheiro
[3] Consultar Extrato
[4] Criar Nova Conta Corrente
[5] Cadastrar Novo Usuário
[6] Listar Todas as Contas
[7] Sair do Sistema
===========================================
=> """
    return input(menu)

# ------------------- Usuários -------------------
def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None
    # Aqui se registra uma pessoa no sistema
def criar_usuario(usuarios):
    while True:
        cpf = input("CPF (somente números, 11 dígitos): ")

        # valida CPF
        if not cpf.isdigit() or len(cpf) != 11:
            print("\n@@@ CPF inválido! Digite exatamente 11 números. @@@")
            continue

        usuario = filtrar_usuario(cpf, usuarios)
        if usuario:
            print("\n@@@ Já existe usuário com esse CPF! @@@")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({
            "nome": nome, 
            "data_nascimento": data_nascimento, 
            "cpf": cpf, 
            "endereco": endereco
        })

        print("\n=== Usuário criado com sucesso! ===")
        break

# ------------------- Contas -------------------
# Aqui se registra uma conta no sistema
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada! @@@")
        return

    print("\n========== LISTA DE CONTAS ==========")
    for conta in contas:
        linha = f"""\
Agência:\t{conta['agencia']}
C/C:\t\t{conta['numero_conta']}
Titular:\t{conta['usuario']['nome']} | CPF: {conta['usuario']['cpf']}
"""
        print("=" * 100)
        print(textwrap.dedent(linha))
    print("======================================")

# ------------------- Operações Bancárias -------------------
def depositar(saldo, extrato):
    while True:
        entrada = input("Informe o valor do depósito: ")
        try:
            valor = float(entrada)
            if valor <= 0:
                print("Operação falhou! O valor deve ser maior que zero.")
            else:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("=== Depósito realizado com sucesso! ===")
                break
        except ValueError:
            print("Entrada inválida! Digite apenas números válidos.")
    return saldo, extrato

def sacar(saldo, extrato, limite, LIMITE_SAQUES, numero_de_saques):
    while True:
        try:
            valor = float(input("Informe o valor do saque: "))
            
            if valor <= 0:
                print("Operação falhou! O valor deve ser maior que zero.")
                continue

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_de_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_de_saques += 1
                print("=== Saque realizado com sucesso! ===")
                break
        except ValueError:
            print("Entrada inválida! Digite apenas números válidos.")

    return saldo, extrato, numero_de_saques

def mostrar_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato, end="")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# ------------------- Programa Principal -------------------
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "2":
            saldo, extrato, numero_saques = sacar(
                saldo, extrato, limite, LIMITE_SAQUES, numero_saques
            )

        elif opcao == "3":
            mostrar_extrato(saldo, extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            criar_usuario(usuarios)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            print("Saindo do sistema... Obrigado por usar nosso banco!")
            break

        else:
            print("Operação inválida, por favor selecione novamente.")

main()
