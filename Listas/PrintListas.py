produtos = ['tv',  'mouse', 'teclado', 'tablet']
vendas=[1000,350,270,900]

listaProdutosSeparados = ' '.join(produtos)
print(listaProdutosSeparados)

listaProdutosSeparados = '; '.join(produtos)
print(listaProdutosSeparados)

listaProdutosSeparados = ' \n '.join(produtos) #dando um enter
print(listaProdutosSeparados)


# split faz o contrario, transforma uma string em um array

lista = " arroz, feijao, leite, pao, carro"
novalista3 = lista.split(',')
print(novalista3)


#count
quantMouseLista = produtos.count('mouse')
print(quantMouseLista)

#clear apaga tudo da lista
# - list.clear()<br>
# Remove todos os itens de uma lista

# Uso:
#     vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']
#     vendedores.clear()
# Resultado:
#     vendedores = []
