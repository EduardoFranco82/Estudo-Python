'''Não confie na ordem dos dicionários, use as chaves
Python Versões Antigas x Versões Novas
Dicionários eram "sem ordem". Atualmente tem ordem, mas o certo é usar as chaves
2 formas de pegar um valor:
dicionario[chave]
.get(chave)'''

mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

# Qual foi o item mais vendido nas categorias 'livros' e 'lazer'?
# Quanto foi vendido de 'notebook asus' e de 'ipad'?

print('o item mais vendido na categoria livro foi {}'.format(mais_vendidos.get('livros')))
print('o item mais vendido na categoria lazer foi {}'.format(mais_vendidos.get('lazer')))

#fazendo agora com o valor
print('a quantidade de notebook asus vendido foi {}'.format(vendas_tecnologia['notebook asus']))
print('a quantidade de ipad vendido foi {}'.format(vendas_tecnologia['ipad']))


# quando faz com get e nao encontra da none

if vendas_tecnologia.get('copo') == None:
    print('copo nao esta dentro da lista de produtos de tecnologia')
else:
    print(vendas_tecnologia.get('copo'))

