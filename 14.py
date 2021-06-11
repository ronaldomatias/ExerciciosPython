numero_real = float(input("Digite um número real positivo: "))

while numero_real < 0:
    print("Número inválido, tente novamente")
    numero_real = float(input("Digite um número real positivo: "))

if numero_real >= 0:
    print("Número válido")



