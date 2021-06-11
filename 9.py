#Elabore um algoritmo  que leia  um conjunto indeterminado  de valores e informe, ao final, o maior e o menor valor lidos.

valor = 1
maior = menor = 0
contador = 0

while (valor > 0):
    valor = float(input("Digite um valor acima de 0. Para cancelar digite um valor < 1: "))
    if contador == 0:
        maior = menor = valor
        contador += 1

    elif (valor < menor) and valor > 0:
        menor = valor
        contador += 1

    elif valor > maior:
        maior = valor
        contador += 1


print(f"O maior foi: {maior}, e o menor foi: {menor}")
