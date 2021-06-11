massa = 0
while massa < 0.5:
    massa = float(input("Digite a massa(gr) e maior que 0.5: "))

tempo = 0
while (massa >=0.5):  #No 1º loop ele armazena massa em massa_inicial e a cada loop vai dividindo a massa por 2 até chegar em < 0.5.
    tempo += 50
    if tempo == 50:
        massa_inicial = massa
    massa = massa/2

print("Massa inicial:", massa_inicial)
print("Massa final:", massa)
print(f"Levou: {(tempo/60)/60:.2f}horas, {tempo/60:.2f} min e {tempo} seg para que a massa/2 chegue abaixo de 0.5")




