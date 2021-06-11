#Faca um programa que solicita ao usuario dois valores inteiros e positivosque serao a base e o expoente

base = -1
expoente = -1

while (base < 0) or (expoente < 0):
    print("Os valores precisam ser acima de -1")
    base = int(input("Digite a base para calcular a pontenciação (maior ou igual a 0): "))
    expoente = int(input("Digite o expoente para calcular a potenciação (maior ou igual a 0): "))
    resultado = (base**expoente)
print(resultado)
