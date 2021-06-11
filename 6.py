#Faca  um  programa  que  calcula  o  produto  dos  numeros  digitados  pelo usuario.

valor = 7
produto = 1

while (valor != 0):
    valor = int(input("Digite um valor: "))
    produto *= valor
    print("O produto dos números inseridos é:", produto)
    print("Digite 0 para encerrar ")
