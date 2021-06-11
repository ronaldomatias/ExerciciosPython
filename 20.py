soma_pares = 0
soma_impares = 0
valor = 0

while valor <= 1000:
    print("Para cancelar, insira um valor acima de 1000.")
    valor = int(input("Digite um valor do tipo inteiro: "))

    if (valor%2 == 0) and (valor < 1000):
        soma_pares = valor + soma_pares
    if (valor%2 == 1) and (valor < 1000):
        soma_impares = valor + soma_impares

print("A soma dos pares foi: ", soma_pares)
print("A soma dos ímpares foi: ", soma_impares)