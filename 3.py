#Escreva um programa que lê 15 valores reais, encontra o maior e o menor deles e mostra o resultado.


menor = maior = 0

for contador in range(1, 15):
    valor = float(input("Digite um valor: "))

    if contador == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print(f"O maior valor foi {maior} e o menor foi {menor}")
