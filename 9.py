A = float(input("Digite o valor para A: "))
B = float(input("Digite o valor para B: "))
C = float(input("Digite o valor para C: "))
D = float(input("Digite o valor para D: "))
#quem é menor
if A < B and A < C and A < D:
    menor = A

if B < A and B < C and B < D:
    menor = B

if C < A and C < B and C < D:
    menor = C

if D < A and D < B and D < C:
    menor = D
#Quem é maior
if A > B and A > C and A > D:
    maior= A

if B > A and B > C and B > D:
    maior = B

if C > A and C > B and C > D:
    maior = C

if D > A and D > B and D > C:
    maior = D

print(f"O maior número foi: {maior} e o menor número foi: {menor}")











