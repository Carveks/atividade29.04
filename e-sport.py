idade = int(input("Qual sua idade ? "))
if idade >= 12 and idade <= 14:
    print("Mirim")
elif idade >= 15 and idade <= 17:
    print("Júnior")
elif idade >= 18 and idade <= 25:
    print("Profissional")
elif idade > 26:
    print("Master")
else:
    print("Você é muito novo :/")