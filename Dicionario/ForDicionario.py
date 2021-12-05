#for sempre retorna a chave

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

#demonstrando o for

for chave in vendas_tecnologia:
    print('a chave {} vendeu o valaor {}'.format(chave, vendas_tecnologia[chave]))



# Qual o valor de notebook vendidos?

notebookVendido = 0

for chave in vendas_tecnologia:
    if 'notebook' in chave:
        notebookVendido += vendas_tecnologia[chave]

print(notebookVendido)