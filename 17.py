repeticoes = int(input("Deseja ver quantos elementos da sequência de Fibonacci? "))

num1 = 0
num2 = 1
contador = 1

while contador <= repeticoes:
    num3 = num1 + num2
    print(f'{num1} ', end='')
    num1 = num2
    num2 = num3
    contador += 1