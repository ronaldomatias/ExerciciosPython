valor = float(input("Valor do produto: "))
tipo_pg = int(input("Forma de pagamento: \nDigite: 1, para pg à vista (dinheiro ou cheque) c/ 10% desc\nDigite: 2, para pg à vista (crédito) c/ 15% desc \nDigite: 3, para pg em 2x s/juros\n"))

if tipo_pg == 1: #var_tipo_pg = 1 (10%desc)
    valor_final = (valor - (valor*10/100))
    print(f"Sua compra foi de: R$ {valor_final}")

elif tipo_pg == 2: #var_tipo_pg = 2 (15%desc)
    valor_final = (valor - ((valor*15)/100))
    print(f"Sua compra foi de: R$ {valor_final}")

elif tipo_pg == 3: #var_tipo_pg = 3 (2x s/juros)
    valor_final = (valor)
    valor2x = valor / 2
    print(f"Sua compra foi de: R$ {valor_final} com 2x parcelas s/juros de R$ {valor2x}")

else:
    print("Fim")