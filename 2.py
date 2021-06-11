nome = input("Qual seu nome? ")
print()
sexo = int(input("Qual seu sexo? MASCULINO (digite: 1) ou FEMININO (digite: 2): "))
print()
estado_civil = int(input("Qual seu estado civil? Solteiro (digite: 1), Casado (digite: 2), Divorciado (digite: 3): "))
print()

if sexo == 2 and estado_civil == 2:     #2 = feminino   ;   2 = casado
    tempo_casado = float(input("Quanto anos de casamento?"))
    tempo_casado = int(tempo_casado)  #arredondando valor pra baixo
    print(f"Seu nome é {nome},você é do sexo feminino e é casada há {tempo_casado} anos")

else:
    print("Só me interesa as casadas")



