numero = int(input("Digite um número inteiro: "))
impar = par = 0

for contador in range (1, 11):
    soma = contador + numero
    if (contador + numero)%2 == 1:
        print(f"Próximos números ímpares: {soma}")

for contador in range (1, 11):
    soma = contador + numero
    if (contador + numero)%2 == 0:
        print(f"Próximos números pares: {soma}")
