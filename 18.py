# CALCULADORA 

print("OBS: O primeiro valor é sobre o segundo. ")
valor1 = float(input("Digite o valor 1: "))
valor2 = float(input("Digite o valor 2: "))

operacao = int(input("Selecione a operação: 1 para SOMAR, 2 PARA MULTIPLICAR, 3 PARA DIVIDIR, 4 PARA POTÊNCIA: "))

if operacao == 1:
    resultado = valor1 + valor2
    print(resultado)
if operacao == 2:
    resultado = valor1 * valor2
    print(resultado)
if operacao == 3:
    resultado = valor1 / valor2
    print(resultado)
if operacao == 4:
    resultado = valor1 ** valor2
    print(resultado)