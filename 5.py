#Faca um algoritmo que solicite um valor para o usuario, e gere a tabuada deste valor.

valor = int(input("Escolha um valor de 1 - 10 para saber sua tabuada: "))


for contador in range (1, 11):
    tabuada = valor * contador
    print(f'{valor} x {contador} = {tabuada}')
    contador += 1