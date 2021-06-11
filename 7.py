vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma_quadrados = 0
for c in range (0, 10):
    vetor_atual = (vetor[0+c])
    quadrado = vetor_atual*vetor_atual
    soma_quadrados += quadrado
print(soma_quadrados)
