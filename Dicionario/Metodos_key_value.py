'''Métodos importantes:
.keys() -> uma "lista" com todas as chaves do dicionario

.values() -> uma "lista" com todos os valores do dicionario

Obs: Se o dicionario for modificado, automaticamente essas variáveis são modificadas, mesmo tendo sido criadas anteriormente'''





vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000,
 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000,
  'tv philco': 2500, 'notebook hp': 1000}

chaves = vendas_tecnologia.keys()
valores = vendas_tecnologia.values()
vendas_tecnologia['eduphone'] = 10 #o ruim de usar assim, e que tudo que fizer, modifica nas variaveis que fez, portando e bom tranformar em lista
print(chaves)
print(valores)
print(list(chaves))
print(list(valores))

#para organizar

lista_chaves = list(chaves)
lista_chaves.sort()
print(lista_chaves)

for chave in lista_chaves:
    print('{}: {} unidades'.format(chave, vendas_tecnologia[chave]))    