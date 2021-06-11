#Dado um n ́umeroninteiro e positivo, dizemos que n ́e perfeito se n for igual `a soma de seus divisores positivos diferentes  de n.

numero = int(input("Digite um número para verificar se é perfeito: "))
contador = 1
soma = 0

while (contador < numero):
    if (numero%contador) == 0:
        soma = soma + contador
        contador = (contador +1)
    else:
        contador = (contador + 1)

if soma == numero:
    print("Numero é perfeito")
else:
    print("O número não é perfeito")

