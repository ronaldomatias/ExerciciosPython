A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
#calculo do DELTA:
delta = B**2 - 4*A*C

if delta >=0:
    x1 = (-B - delta**0.5) / (2*A)
    x2 = (-B + delta**0.5) / (2*A)
    print(f"O valor de delta é: {delta}")
    print(f"X1 = {x1}")
    print(f"X2 = {x2}")
else:
    print("Delta menor que 0, logo, número negativo não possui raiz:  - * - = +")
