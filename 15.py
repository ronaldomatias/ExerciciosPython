# identificacao aluno
id = int(input("Código do aluno: "))
#inserir nota 1, 2, 3.
nota1 = int(input("Digite a nota1 (0-100): "))
nota2 = int(input("Digite a nota2 (0-100): "))
nota3 = int(input("Digite a nota3 (0-100): "))
#total pontos exercícios
exercicios = int(input("Digite a soma das notas dos 3 exercícios (0 a 300): "))
ME = round((exercicios / 3),2)
#conversão para a média
#Média das notas
MA = float(((((nota1+nota2*2)) + (nota3*3))/6))
MA = round(((MA + ME) /2),2)



if MA >= 90:
    print(f"Aluno: {id}\nNota1: {nota1}\nNota2: {nota2}\nNota3: {nota3}\nMédia dos exercícios: {ME}\nMédia de aproveitamento: {MA}\nSituação: APROVADO com nota A ")

elif MA >= 75 and MA <90:
    print(f"Aluno: {id}\nNota1: {nota1}\nNota2: {nota2}\nNota3: {nota3}\nMédia dos exercícios: {ME}\nMédia de aproveitamento: {MA}\nSituação: APROVADO com nota B ")

elif MA >=60 and MA <75:
    print(f"Aluno: {id}\nNota1: {nota1}\nNota2: {nota2}\nNota3: {nota3}\nMédia dos exercícios: {ME}\nMédia de aproveitamento: {MA}\nSituação: APROVADO com nota C ")

elif MA >= 40 and MA < 60:
    print(f"Aluno: {id}\nNota1: {nota1}\nNota2: {nota2}\nNota3: {nota3}\nMédia dos exercícios: {ME}\nMédia de aproveitamento: {MA}\nSituação: REPROVADO com nota D ")

elif MA < 40:
    print(f"Aluno: {id}\nNota1: {nota1}\nNota2: {nota2}\nNota3: {nota3}\nMédia dos exercícios: {ME}\nMédia de aproveitamento: {MA}\nSituação: REPROVADO com nota E ")

print