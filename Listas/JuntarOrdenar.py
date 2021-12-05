produtos = ['tv',  'mouse', 'teclado', 'Tablet']
vendas=[1000,350,270,900]

#extend vai juntar em uma das listas
produtos.extend(vendas)
print(produtos)

#pra fazer uma nova lista

novaLista = produtos + vendas
print(novaLista)

#nao usar append para adicionar listas, porque apende adiciona uma lista em outra

produtos.append(vendas)
print(produtos)

#tomar cuidado

#[1] + [2] =! de 1 + 2
print([1] + [2]) # => da uma nova lista
print (1 +2)

somaTvMouse = vendas[0] + vendas [1]
print(somaTvMouse)

#ordenar listas tomar cuidado pois python puxa pela tabela asc e faz diferença maiusculo minusculo
novaLista2 = ['casa','predio','Mercado', 'açougue']
novaLista2.sort()
print(novaLista2)

vendas.sort()
print(vendas)
#jeito invertido

vendas.sort(reverse= True)
print(vendas)

