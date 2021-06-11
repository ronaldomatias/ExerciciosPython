total_vendas = vendas = total_comissao1 = 0

while vendas >= 0:
    vendas = float(input("Insira o valor das vendas do funcionário (digite um numero negativo para sair): "))

    if vendas >=0:
        total_vendas += vendas

    if vendas >= 3000 and vendas >= 0:
        comissao = (35*vendas)/100
        print(f"A comissão foi de 35%: {comissao}")
        total_comissao1 += comissao

    if vendas >= 1500 and vendas < 3000 and vendas >= 0:
        comissao = (20*vendas)/100
        print(f"A comissão foi de 20%: {comissao}")
        total_comissao1 += comissao

    if vendas < 1500 and vendas >= 0:
        comissao = (13*vendas)/100
        print(f"A comissão foi de 13%: {comissao}")
        total_comissao1 += comissao

print(f"Total de vendas da empresa: {total_vendas}")
print(f"Total de comissão pagos: {total_comissao1}")




