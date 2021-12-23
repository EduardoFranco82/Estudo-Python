lista = [10,20,30]

for i, item in enumerate(lista) :# enumerate para criar indices
    item += 5
    lista[i]= item
    print(lista)


def padronizar_codigos(lista_codigos, padrao='m'):
    for i, item in enumerate(lista_codigos):
        item = item.replace('  ', ' ')
        item = item.strip()
        if padrao == 'm':
            item = item.casefold()
        elif padrao == 'M':
            item = item.upper()
        lista_codigos[i] = item
    return lista_codigos


cod_produtos = [' ABC12 ', 'abc34', 'AbC37']
print(padronizar_codigos(cod_produtos))


palavra = ' ededed '
palavra = palavra.strip()
print(palavra)

palavra2 = ' edu edu edu'
palavra2 = palavra2.replace(' ', '')
print(palavra2)