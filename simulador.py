inv = float(input("Quanto deseja investir ? "))
prazo = float(input("Em qual prazo ? "))
if prazo > 12: 
    print("Sua taxa será de 12% ao ano")
else: 
    print("Sua taxa será de 8% ao ano")