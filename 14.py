# identificacao aluno
id = int(input("Código do aluno: "))
#inserir nota 1, 2, 3.
nota1 = int(input("Digite a nota1 (0-100): "))
nota2 = int(input("Digite a nota2 (0-100): "))
nota3 = int(input("Digite a nota3 (0-100): "))
#total pontos exercícios
exercicios = float(input("Digite a soma das notas dos 3 exercícios (0-300): "))
ME = round((exercicios/3),2)
#Média das notas
MA = float(((((nota1+nota2*2)) + (nota3*3))/6))
MA = round(((MA + ME) /2),2)
print(f"Aluno: {id}\nMA: {MA:.2f}")

