nome = input("Nome do cliente: ")
dias = int(input("Quantos dias o cliente ficou hospedado? "))
diaria = 300

if dias < 15: #taxa de 20,00 dia
    total = (dias*diaria) + (20*dias)
    print(f"{nome}, sua conta é de: {total}")

if dias == 15: #taxa de 14,00 dia
    total = (dias*diaria) + (14*dias)
    print(f"{nome}, sua conta é de: {total}")

if dias > 15: #taxa de 20,00 dia
    total = (dias*diaria) + (12*dias)
    print(f"{nome}, sua conta é de: {total}")
