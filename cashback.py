valor = float(input("Qual o valor de sua compra ? "))
if valor > 500:
    res = (valor * 10) / 100
    print (f'Seu cashback será de {res}' )
elif valor >= 200 and valor <= 500:
    res = (valor * 5) / 100
    print (f'Seu cashback será de {res}' )
else:
    print("Não terá cashback em sua compra :/")
