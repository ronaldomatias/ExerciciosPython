#Faca um programa que solicita ao usúario uma quantidade indeterminada de ńumeros inteiros e tira a média dos pares.

valor = 1
soma = 0
contador = 0
media = 0

while valor != 0:
    valor = int(input("Digite um valor inteiro (ou 0 para cancelar) : "))

    if (valor%2 == 0) and (valor != 0):
        soma += valor
        contador += 1
        media = (soma / contador)
print("A média dos pontos pares foi de: ", media)





