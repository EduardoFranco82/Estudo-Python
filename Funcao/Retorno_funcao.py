def cadastrar_produto():
    produto = input('digite o produto:')
    produto = produto.casefold()#transforma tudo em minuculo
    #print('o produto cadastrado foi {}'.format(produto_cadastrado))## print nao deve estar dentro de uma funcao
    produto = produto.strip()#retira os espaços
    return produto


produto = cadastrar_produto()
print(produto)
