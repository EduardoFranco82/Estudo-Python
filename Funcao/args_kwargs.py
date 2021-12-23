'''Quantidade Indefinidas de Argumentos
Utilidade:
Quando você quer permitir uma quantidade indefinida de argumentos, usa o * para isso.

Estrutura:
*args para positional arguments -> argumento em formato de tupla
def minhafuncao(*args):


**kwargs para keywords arguments -> argumento vem em formato de dicionario

def minhafuncao(**kwargs):
    

'''

def minha_soma(*numeros):
    print(numeros) #retorna uma tupla
    soma = 0
    for i in numeros:
        soma += i
    return soma

soma = minha_soma(1,2,3,4,5)
print(soma)



def preco_final(preco, **adicionais):# retorna um dicionario
    print(adicionais) #printa o dicionario
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra'] 
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco