def cadastrar_produto():
    produto = input('digite o produto:')
    produto_cadastrado = produto.casefold()#transforma tudo em minuculo
    print('o produto cadastrado foi {}'.format(produto_cadastrado))

#cadastrar_produto()

for i in range (3):
    cadastrar_produto()