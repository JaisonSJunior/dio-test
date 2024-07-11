def menu():
    menu_text = """
[1] Extrato
[2] Depositar
[3] Sacar
[4] Listar Contas
[5] Nova Conta
[6] Novo Usuário
[0] Sair
""" 
    return input(menu_text)

def depositar(saldo, valor, extrato, /):
    try:
        val = int(valor)
        if val <= 0:
            print("\n Insira um valor válido.")
        else:
            saldo += val
            print(f"\n O valor de R${val}.00 foi adicionado ao seu saldo. Saldo atual é de: R${saldo:.2f}.")
            extrato += f"Depósito: R${val}.00 \n"
    except ValueError:
        print("\n Valor inválido. Por favor, tente novamente.")
    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("\n Limite de saques diários excedido, tente novamente amanhã.")
    else:
        print(f"Você ainda possui {limite_saques - numero_saques} saques hoje.")
        user_input = input("Insira a quantia a ser sacada em reais:")
        try:
            val = int(user_input)
            if val <= 0:
                print("\n Insira um valor válido.")
            elif val > saldo:
                print("\n Saldo insuficiente. Tente novamente.")
            elif val > limite:
                print("\n O valor é maior que o limite de R$500.00 por saque.")
            else:
                saldo -= val
                numero_saques += 1
                print(f"\n O valor de R${val:.2f} foi sacado de seu saldo. Saldo atual é de: R${saldo:.2f}.")
                extrato += f"Saque: R${val:.2f} \n"
        except ValueError:
            print("\n Valor inválido. Por favor, tente novamente.")
    return saldo, extrato, numero_saques

def imprimir_extrato(saldo, /, *, extrato):
    print("================Extrato================")
    print("Não há movimentações" if not extrato else extrato)
    print(f"\n Saldo: R${saldo:.2f}")
    print("=======================================")

def criar_usuario(usuarios):
    cpf = input("Informe apenas os números do CPF (sem pontos, traços ou espaços):")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Usuário já cadastrado.")
        return
    nome = input("Informe o nome completo:")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla do estado):")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "CPF": cpf, "endereco": endereco})
    print("Usuário criado com sucesso")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]  
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe apenas os números do CPF (sem pontos, traços ou espaços):")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuario inexistente. Favor criar cadastro antes")

def listar_contas(contas):
    for conta in contas:
        dados = f"""
Agência: {conta['agencia']}
Conta: {conta['numero_conta']}
Usuário: {conta['usuario']['nome']}
"""
        print(dados)

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    agencia = "0001"
    usuarios = []
    contas = []
    contador_contas = 1

    while True:
        option = int(menu())

        if option == 0: # Sair
            break
        elif option == 1: # Extrato
            imprimir_extrato(saldo, extrato=extrato)
        elif option == 2: # Depositar
            user_input = input("Insira a quantia a ser depositada em reais, sem os centavos:")
            saldo, extrato = depositar(saldo, user_input, extrato)
        elif option == 3: # Sacar
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques,
            )
        elif option == 4: # Listar Contas
            listar_contas(contas)
        elif option == 5: # Nova Conta
            conta = criar_conta(agencia, contador_contas, usuarios)
            if conta:
                contas.append(conta)
                contador_contas += 1
        elif option == 6: # Novo Usuário
            criar_usuario(usuarios)
        else:
            print("Opção Inválida, favor tentar novamente.")

    print("\n Obrigado por usar nossos Serviços!")

if __name__ == "__main__":
    main()
