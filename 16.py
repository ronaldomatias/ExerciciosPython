A = float(input("Valor 1: "))
B = float(input("Valor 2: "))
C = float(input("Valor 3: "))
#equilátero = 3 LADOS IGUAIS  /  escaleno = 3 LADOS DIFERENTES   / isósceles = 2 LADOS IGUAIS.

if A < B+C and B < A+C and C < A+B:
    print("Triângulo pode ser formado")
    if A == B and A == C:
        print("O triângulo é Equilátero")
        if A != B and A != C and B != C:
            print("O Triângulo é Isósceles")
            if A != B and A != C and B != C:
                print("Triângulo Escaleno")

else:
    print("Triângulo não pode ser formado")

