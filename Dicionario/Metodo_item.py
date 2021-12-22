'''Métodos úteis em dicionários
items() dos dicionários'''

#itens retorna uma lista de tuplas



vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000,
 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000,
  'tv philco': 2500, 'notebook hp': 1000}

#print (vendas_tecnologia.items())

for produto, qtdade in vendas_tecnologia.items():
   print ('produto: {}, quantidade: {}'.format (produto, qtdade))


'''Quais produtos venderam mais de 5000 unidades?'''
for produto, qtdade in vendas_tecnologia.items():
    if qtdade > 5000:
        print(produto)

# 2 forma de fazer
for chave in vendas_tecnologia:
    if vendas_tecnologia[chave] > 5000:
        print('{}: {} unidades'.format(chave, vendas_tecnologia[chave]))


