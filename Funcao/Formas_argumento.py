'''Mais de 1 argumento e formas de passar argumento para uma função
Estrutura:
2 formas de passar o argumento:
Em ordem (positional argument) QUANDO FAZ ASSIM, TEM QUE RESPEITAR AS ORDENS
Com o nome do argumento (keyword argument) QUANDO FAZ ASSIM NAO IMPORTA A ORDEM,
POREM TEM QUE TIPAR TODOS ARGUMENTOS'''

def eh_categoria (produto, codigo):
    produto = produto.upper()
    if codigo in produto:
        return True
    else:
        return False


produtos = ['CAR46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

for produto in produtos:
    if eh_categoria(produto, codigo= 'BEB'):
        print('produto {} e bebida alcoolica'.format(produto))
    elif eh_categoria(produto, 'BSA'):
        print('produto {} nao e bebida alcoolica'.format(produto))



#Descobrindo a quantidade de produtos usando sep

qtdade_produtos = len(produtos)
print(qtdade_produtos)

print('a quantidade de produtos e ', qtdade_produtos, 'eduardo que fez', sep = '\n')