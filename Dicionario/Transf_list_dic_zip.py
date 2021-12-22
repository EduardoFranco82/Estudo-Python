'''Transformando Listas em Dicionários e Function zip
Estrutura:
Dicionário com valores padrões:
dicionario = dict.fromkeys(lista_chaves, valor_padrao)

Dicionário a partir de listas de tuplas:
dicionario = dict(lista_tuplas)

Dicionário a partir de 2 listas:
Passo 1: Transformar listas em lista de tuplas com o método zip
Passo 2: Transformar em dicionario

lista_tuplas = zip(lista1, lista2)
dicionario = dict(lista_tuplas)'''

#para transformar 2 listas em um dicionario
produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']
vendas = [15000, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450]

lista_tuplas = zip(produtos, vendas)
dicionario_vendas = dict(lista_tuplas)
print(dicionario_vendas)



#Quanto vendemos de ipad?
# Fazendo por lista
index = produtos.index('ipad')
print(index)
print('vendemos {} ipad'.format(vendas[index]))

#fazendo por dicionario LEMBRNADO QUE DICIONARIO E CHAVE VALOR
print('vendemos {} ipads'.format(dicionario_vendas['ipad']))
print('vendemos {} iphone'.format(dicionario_vendas['iphone']))