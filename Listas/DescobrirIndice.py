produtos = ['tv',  'mouse', 'teclado', 'tablet']
vendas=[1000,350,270,900]

#pegando o index
i = produtos.index('teclado')
print(i)

quantVendas = vendas[2]
print(quantVendas)

produto = input ('insira o nome do produto em letra minuscula')
if produto in produtos:
        index = produtos.index(produto)
        qutvendas = vendas[index]
        print(index)
else:
    print ('produto nao existe')