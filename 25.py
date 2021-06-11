passo = 0

numero = int(input("Digite um número inteiro para saber os próximos primos: "))

while passo < 10:
    if passo > 0:
        numero = numero +1

    divisores = 0
    for contador in range (1, numero+1):

        if numero%contador == 0:
            divisores += 1

    if divisores == 2 and numero > 0:
        print(f"{numero} é primo.")
        passo += 1
    else:
        print(numero)
        passo += 1





