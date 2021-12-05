vendas = [100, 150, 1500, 2000,120]

meta = 110
#pra nao precisar percorrer tudo
for venda in vendas:
    if venda < meta:
        print('a loja nao ganhou bonus')
        break
    print(venda)


vendedores = [ 'joao', 'julia', 'ana', 'jose', 'maria']
meta2 = 130


for venda in vendas:
    if venda < meta2:
        continue # nao faça nada
    print(venda)