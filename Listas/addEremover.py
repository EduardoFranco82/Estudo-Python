produtos = ['tv',  'mouse', 'teclado', 'tablet']
vendas=[1000,350,270,900]


#adicionando
print(produtos)
produtos.append('videogame')
print(produtos)


#removendo
produtos.remove('videogame')
print(produtos)

#removendo com pop, ele armazena o item removido, para remover com pop, precisa usar o index

item_removido = produtos.pop(0)
print(item_removido)
print(produtos)

try:
    produtos.remove('casadavovo')
except:
        print('produto nao encontrado')
        #pass
