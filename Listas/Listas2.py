produtos = ['tv',  'mouse', 'teclado', 'tablet']
vendas=[1000,350,270,900]


print ('vendas do produto {} foram de {} unidades'.format(produtos[0], vendas[0]))

#modificando

vendas[3] = 1000
print(vendas)

#pra string nao funciona

texto = 'eduardo'
#texto[2] = 'a' -> nao aceita

texto = texto.replace('e', 'i')

print(texto)
