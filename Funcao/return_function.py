#tomar cuidado com return dentro de funçao

'''Mais sobre o return
Pontos importantes:
Podemos usar no return praticamente qualquer tipo de objeto:
 (número, string, lista, tupla, dicionário, outros objetos, etc.)
O return, se for executado, encerra a função, mesmo que dentro dela haja um loop.'''


#retornar um número
def minha_soma(num1, num2, num3):
    return num1 + num2 + num3

#retornar um texto
def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace("  ", " ")
    texto = texto.strip()
    return texto

#retornar um boolean
def bateu_meta(vendas, meta):
    if vendas >= meta:
        return True
    else:
        return False
    
#retornar uma lista, tupla ou dicionario
def filtrar_lista_texto(lista, pedaco_texto):
    lista_filtrada = []
    for item in lista:
        if pedaco_texto in item:
            lista_filtrada.append(item)
    return lista_filtrada                # se colocar esse return dentro do if, ele vai retornar o primeiro valor e vai parar o loop


lista_textos = ['lira@gmail.com', 'zezinho@hotmail.com', 'joao@gmail.com', 'alon@gmail.com']

lista_filtrada = filtrar_lista_texto(lista_textos, 'gmail')
print(lista_filtrada)