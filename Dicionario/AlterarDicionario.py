'''Adicionar, Remover e Modificar Itens no Dicionário
Estrutura:
Adicionar itens:'''


lucro_1tri = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
lucro_2tri = {'abril': 88000, 'maio': 89000, 'junho': 120000}
#adicionando 1 item
lucro_1tri['dezembro'] = 60000
print(lucro_1tri)
#lucro_1tri['abril'] = 88000
#print(lucro_1tri)
#adicionando vários itens ou um dicionário a outro
lucro_1tri.update({'abril': 88000, 'maio': 89000, 'junho': 120000})
lucro_1tri.update({'mesquevem': 5, 'mesquevemquevem' : 6})
print(lucro_1tri)
#adicionando um item já existente (manualmente ou pelo update)
lucro_1tri['janeiro'] = 88000
print(lucro_1tri)


'''Modificar itens:
Da mesma forma que adicionamos 1 valor, caso essa chave já exista o item é apenas modificado.

dicionario[chave] = valor

Vamos modificar o lucro de fevereiro:
(Lembrando: caso o item não exista, ele vai criar o item no dicionário)'''

lucro_1tri['janeiro'] = '123456'
print(lucro_1tri)


'''
Remover itens:
del dicionario[chave]

ou então

valor = dicionario.pop(chave)

mas cuidado com:

del dicionario
-> que é diferente de dicionario.clear()'''

lucro_junho = lucro_1tri.pop('junho')
print(lucro_1tri)
print(lucro_junho)
# clear limpa todo dicionario, mas nao exclui o dicionario
lucro_1tri.clear()
print(lucro_1tri)

#del apaga o dicionario

del lucro_2tri['maio']
print(lucro_2tri)

#agora apaga tudo
del lucro_2tri
print (lucro_2tri)# da erro
