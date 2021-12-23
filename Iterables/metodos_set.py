#add -> adiciona um item no set
meu_set = {'iphone', 'macbook', 'ipad'}
meu_set.add('airpod')
print(meu_set)

#remove -> retira um item de um set
meu_set = {'iphone', 'macbook', 'ipad'}
meu_set.remove('iphone')
print(meu_set)

#clear -> retira todos os itens de um set
meu_set = {'iphone', 'macbook', 'ipad'}
meu_set.clear()
print(meu_set)

#union -> junta as informações de 2 sets. Se houver algum valor duplicado, ele constará apenas 1 vez no set final
produtos = {'iphone', 'macbook', 'ipad'}
lancamentos = {'airpod', 'apple watch', 'ipod', 'ipad'}
todos_produtos = produtos.union(lancamentos)
print(todos_produtos)

#intersection -> pega apenas as informações que existem nos 2 sets ao mesmo tempo
produtos = {'iphone', 'macbook', 'ipad'}
lancamentos = {'airpod', 'apple watch', 'ipod', 'ipad'}
intersecao = produtos.intersection(lancamentos)
print(intersecao)

#difference -> retorna todas as informações de um set que não fazem parte de outro set
produtos = {'iphone', 'macbook', 'ipad'}
lancamentos = {'airpod', 'apple watch', 'ipod', 'ipad'}
produtos_nao_lancamentos = produtos.difference(lancamentos)
print(produtos_nao_lancamentos) #repare que ipad foi retirado do resultado porque ele estava contido no set de lançamentos