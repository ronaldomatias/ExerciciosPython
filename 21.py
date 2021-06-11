valor1 = float(input("Digite o valor 1: "))
valor2 = float(input("Digite o valor 2: "))
valor3 = float(input("Digite o valor 3: "))

if (valor1 < valor2) and (valor2 < valor3) and (valor1 < valor3):
    soma = valor1 + valor2 + valor3
    multiplicacao = valor1 * valor2 * valor3
    media = ((valor1 + valor2 + valor3) / 3)

    print(f"Soma dos 3 valores: {soma:.2f}")
    print(f"Multiplicação dos 3 valores: {multiplicacao:.2f}")
    print(f"Média dos 3 valores: {media:.2f}")

else:
    print("Digite os valores em ordem crescente.")



