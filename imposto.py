valor = float(input("Digite o valor do produto que você comprou: "))
if valor > 50:
    res = valor + (valor*60)/100
    print(f'O valor do seu produto com imposto é de {res}')
else:
    res = valor + (valor*17)/100
    print(f'O valor do seu produto com imposto é de {res}')