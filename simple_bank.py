menu = f"{" Menu ".center(46,"#")}"
print(menu)
print("""
Selecione uma opção abaixo
      
      [d] : Depositar

      [s] : Sacar

      [e] : Extrato

""")
print("#"*46)
saldo = 0

transacoes = 0
MAX_TRANSACAO = 3

while True:
    opcao = input("digite a opção desejada: ").lower()

    match opcao:

        case "d":
            