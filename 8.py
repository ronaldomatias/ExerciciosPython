#Construa um algoritmo quecalcule e imprima quantos anos serao necessarios para que Ze seja maior que Chico.

tamanho_chico = float(1.5)
tamanho_ze = float(1.1)
contador_anos = 0
while (tamanho_chico > tamanho_ze):
    tamanho_ze += 0.3
    tamanho_chico += 0.2
    contador_anos += 1
print(f"Será necessário {contador_anos} ano(s) para que Zé ultrapasse o tamanho de Chico.")
print(f"O tamanho de Zé ficou {tamanho_ze:.2f} e o tamanho de Chico ficou {tamanho_chico:.2f}")
