altura = float(input("Digite sua altura: "))
sexo = int(input("Qual seu sexo? (Digite: 1 para Masculino) ou (digite: 2 para FEMININO): "))

if sexo == 1:    #var(sexo)= (1 Homem) (2Mulher)
        peso_ideal = round((72.7*altura)-58)
        print(peso_ideal)

elif sexo == 2:    #var(sexo)= (1 Homem) (2Mulher)
        peso_ideal = (round(62.1*altura)-44.7)
        print(peso_ideal)

else:
    print("Leia atentamente o enunciado")

