
valor1 = int(input("Digite um número inteiro: "))
valor2 = int(input("Digite um número inteiro: "))
multiplicacao = 1
pares = 0
for contador in range (valor1,valor2+1):
    if contador%2 == 0:
        pares += contador
print(f"A soma dos números pares entre {valor1} e {valor2} é: {pares}")

for contador in range (valor1, valor2+1):
    if contador%2 == 1:
        multiplicacao *= contador
print(f"A multiplicação dos números ímpares entre {valor1} e {valor2} é: {multiplicacao}")
