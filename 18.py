salario = float(input("Quanto você ganha por mês? "))

emprestimo = float(input("Quanto dinheiro você precisa? (max. 30% do salário): "))


if emprestimo <= (salario*30)/100:
    print(f"Empréstimo concebido no valor de: {emprestimo}")


else:
    print("Valor solicitado ultrapassou 30% do seu salário")
