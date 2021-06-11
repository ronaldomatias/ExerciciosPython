peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))
IMC = round(peso/altura**2)

if IMC < 18.5:
    print(f"IMC: {IMC}kg/m² = Frango")

elif IMC >= 18.5 and IMC < 25:
    print(f"IMC: {IMC}kg/m² = fit")

elif IMC >= 25 and IMC < 30:
    print(f"IMC: {IMC}kg/m² = gordin")

elif IMC >= 30:
    print(f"IMC: {IMC}kg/m² = bariátrica free")