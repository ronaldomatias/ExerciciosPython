
numero = int(input("Digite um número inteiro: "))
divisores = 0

for contador in range (1, numero+1):

    if numero%contador == 0:
        divisores += 1
        print(contador)

if divisores == 2 and numero > 0:
    print("O número é PRIMO.")
else:
    print("O número NÃO É PRIMO.")

