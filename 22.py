menor_media = maior_media = media_alunos = contador = 0

while media_alunos >= 0:
    media_alunos = float(input("Digite as médias dos alunos, uma por uma: "))
    contador += 1

    if contador == 1 and media_alunos >= 0:
        maior_media = menor_media = media_alunos

    if contador > 1 and media_alunos >= 0:
        if media_alunos < menor_media:
            menor_media = media_alunos
        if media_alunos > maior_media:
            maior_media = media_alunos
print(f"A maior média: {maior_media} e a menor média: {menor_media}")

    



