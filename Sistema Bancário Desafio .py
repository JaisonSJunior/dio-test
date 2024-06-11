menu = """

[1] Extrato
[2] Depositar
[3] Sacar
[0] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while 0 == 0:
    
    option = int(input(menu))  

    if option == 0:
        break

    elif option == 1:
        print("================Extrato================")
        print("Não há movimentações" if not extrato else extrato)
        print(f"\n Saldo: R${saldo:.2f}") 
        print("=======================================")
        
    elif option == 2:
           
        user_input = input("Insira a quantia a ser depositada em reais, sem os centavos:")
        try:
            val = int(user_input)
            if val<= 0:
                    print("\n Insira um valor válido.")
            else:
                saldo+= val
                print(f"""\n O valor de R${val}.00 foi adicionado ao seu saldo.
                    Saldo atual é de: R${saldo:.2f}.""")
                extrato += f"Depósito: R${val}.00 \n"
             
        except ValueError:
            print("\n Valor inválido. Por favor, tente novamente.")

    elif option == 3:
        if limite_saques <= numero_saques:
            print("\n Limite de saques diários excedido, tentar novamente amanhã.")
        else:
            print(f"Você ainda possui {limite_saques-numero_saques} saques hoje.")
            user_input = input("Insira a quantia a ser sacada em reais:")
            try:
                val = int(user_input)
                if val<= 0:
                    print("\n Insira um valor válido.") 
                elif val <= saldo:
                    if val <= limite:
                        saldo -= val
                        print(f"""\n O valor de R${val:.2f} foi sacado de seu saldo.
                            Saldo atual é de: R${saldo:.2f}.""")
                        numero_saques += 1                 
                        extrato += f"Saque: R${val:.2f} \n"
                    else:
                        print("\n O valor é maior que o limite de R$500.00 por saque")
                elif val >= saldo:
                    print("\n Saldo Insuficiente. Tente novamente.")
                else:
                    print("\n Insira um valor válido.")            
                
            except ValueError:
                print("\n Valor inválido. Por favor, tente novamente.")

    else:
        print("Opção Inválida, favor tentar novamente.")

print("\n Obrigado por usar nossos Serviços!")