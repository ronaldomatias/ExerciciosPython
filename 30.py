alunos = int(input("Quantos alunos têm na turma: "))
qtdd_notas = int(input("Quantas notas têm cada aluno: "))
maior_media = 0
menor_media = 0

soma_notas = soma_medias = 0
for  qtddalunos in range (1, alunos+1):
    soma_notas = 0
    for qtddnotas in range(1, qtdd_notas + 1):
        nota = float(input("Digite a nota de um aluno por vez: "))

        if nota >= 0:
            soma_notas += nota
    media_aluno = soma_notas / qtdd_notas
    if qtddalunos == 1:
        maior_media = media_aluno
        menor_media = media_aluno
    if media_aluno < menor_media:
        menor_media = media_aluno
    if media_aluno > maior_media:
        maior_media = media_aluno
    soma_medias += media_aluno
    print(f"A média do aluno foi: {media_aluno}")


media_geral = soma_medias / alunos
print(f"A média geral foi: {media_geral}")
print(f"A maior média foi: {maior_media}")
print(f"A menor média foi: {menor_media}")



