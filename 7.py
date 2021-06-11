num = float(input("Digite um valor inteiro: "))
num = int(num)
num2 = int(num) %2

if num2 == 0: #se numero for par, somar +5.
    print(num+5)

if num2 == 1: #se numero for impar, somar +8.
    print(num+8)