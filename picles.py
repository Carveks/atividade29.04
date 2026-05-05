saldo = float(input("Digite seu saldo: "))
ted = float(input("Qual o valor da tranferência ? "))
if saldo > ted:
    print("Transferência realizada")
else:
    cheque = float(input("Você tem cheque especial ? Quanto ? ")) 
    if (saldo + cheque) > ted:
        print("Transferência realizada")
    else:
        print("Saldo insuficiente")