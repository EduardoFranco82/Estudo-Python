def cadastrar_produto():
    produto = input('digite o produto:')
    produto_cadastrado = produto.casefold()  # transforma tudo em minuculo
    #print('o produto cadastrado foi {}'.format(produto_cadastrado))
    return produto_cadastrado


# cadastrar_produto()
lista_produtos = []
for i in range(2):
    lista_produtos.append(cadastrar_produto())

print(lista_produtos)
