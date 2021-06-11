A = float(input("Valor 1: "))
B = float(input("Valor 2: "))
C = float(input("Valor 3: "))
#equilátero = 3 LADOS IGUAIS  /  escaleno = 3 LADOS DIFERENTES   / isósceles = 2 LADOS IGUAIS.

if A > B+C or B > A+C or C > A+B:
    print("Triângulo não pode ser formado")
else:
    if A == B and A == C:
        print("O triângulo é Equilátero")
    elif A != B and A != C and B != C:
        print("Triângulo Escaleno")
    else:
        print("Triângulo isósceles")

