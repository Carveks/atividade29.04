telas = int(input("Quantas telas usará ?"))
if telas == 1:
    print("Plano mobile")
elif telas == 2:
    print("Plano padrão")
elif telas == 4:
    print("Plano premium")
else:
    print("Opção inválida")