valor = float(input("Qual o valor de sua compra? "))

if valor > 500:
    res = valor * 0.10  # 10%
    print(f'Seu cashback será de R$ {res:.2f}')
elif valor >= 200:
    # Se o código chegou aqui, ele já sabe que é <= 500
    res = valor * 0.05  # 5%
    print(f'Seu cashback será de R$ {res:.2f}')
else:
    # Captura QUALQUER valor abaixo de 200 (incluindo 199.99)
    print("Não terá cashback em sua compra :/")