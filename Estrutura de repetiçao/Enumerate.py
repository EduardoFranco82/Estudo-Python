#pra quando vc quer usar chave e valor, ou pegar o indice de uma lista

funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']

#ja da chave valor direto

for i,funcionario in enumerate(funcionarios) :
   print(i, funcionario)
  #  print(i,funcionario)

# da chave e valor entre parenteses
#for funcionario in enumerate(funcionarios):
    #print(funcionario)
# funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']

# for i, funcionario in enumerate(funcionarios):
#     print('{} é o funcionário {}'.format(i, funcionario))

#VERIFICAR QUEM ESTA ABAIXO DO ESTOQUE
estoque = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte', 'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
nivel_minimo = 50

for i, estoque in enumerate(estoque):
    if estoque < nivel_minimo:
        print('o produto {} esta abaixo do estoque com {} unidades'.format(produtos[i],estoque ))