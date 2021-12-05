produtos = ['tv',  'mouse', 'teclado', 'tablet']
vendas=[1000,350,270,900]

tamanhoDaLista = len(produtos)
print(tamanhoDaLista)

maior = max(vendas)
menor = min(vendas)

print(maior, menor)


i =  vendas.index(maior)
produto_com_maior_venda  = produtos[i]
print(produto_com_maior_venda)
