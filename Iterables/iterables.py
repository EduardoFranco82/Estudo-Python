# o que sao iterables
#é quando vc percorre cada elemento de uma lista, de um texto, de um dicionario, ou uma tupla

'''Explicação não programadora
Um iterable é uma estrutura que armazena dados que pode ser "iterada" ou seja, que você pode fazer um loop como um for dentro dela e ir passando de item a item.
É como se fosse um tipo de lista de coisas que você pode ir olhando cada um dos elementos dentro dela.'''

produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']

for produto in produtos:
    print(produto)