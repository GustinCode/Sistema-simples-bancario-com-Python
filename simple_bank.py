saldo = 0
extrato = []
print
transacoes = 0
MAX_TRANSACAO = 3

while True:
    print(f"\n {" Menu ".center(36,"#")}")
    print("""
    Selecione uma opção abaixo
        
        [d] : Depositar

        [s] : Sacar

        [e] : Extrato
        
        [q] : Sair
    """)
    print("#"*36)
    opcao = input("digite a opção desejada: ").lower()

    match opcao:

        case "d":
            valor_deposito = float(input("Digite o valor para deposito: "))
            saldo += valor_deposito
            extrato.append(["Deposito", valor_deposito])
            continue
        case "s": 
            valor_saque = float(input("Valor de saque limitado a 500 reais\nDigite o valor do saque: "))
            if transacoes >= MAX_TRANSACAO:
                print(f"Operação não realizada.\nMaxímo de limite de saque já atingido: {MAX_TRANSACAO}")
                continue
            if valor_saque > 500:
                print("Erro operação não realizada.\nSaque maior que o limite permitido")
                continue
            if valor_saque > saldo:
                print("operação não realizada.\nSaldo insuficiente para realizar a operação")
                continue
            transacoes += 1
            saldo-=valor_saque
            extrato.append(["Saque", valor_saque])
        case "e":
            if extrato is False:
                print("Operação não pode ser realizada\n Não há registros de extrato")
                continue

            print(" Extrato ".center(36, "#")+"\n")
            # utilizar operacao como o item que vai acessar a string no vetor bi dimensional
            for num_operacao in extrato:
                #utilizamos a variavel operação para acessar dentro do vetor bidimensional as informações de extrato. 
                print(f"Tipo de operação: {num_operacao[0]} R$ {num_operacao[1]:.02f}\n")
            print("#"*36)
        case "q":
            print("\nObrigado por acessar o nosso sistema\nTenha um bom dia!")
            exit()

