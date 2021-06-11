#Faca um algoritmo que gere, automaticamente, a tabuada dos valores de 1 a 10.

numerador = 1
multiplicador = 1

for contador in range (0, 100):
    resultado = numerador * multiplicador
    print(f"{numerador} x {multiplicador} = {resultado}")
    multiplicador += 1

    if multiplicador == 11:
        multiplicador = 1
        numerador += 1
        print("-"*10)










