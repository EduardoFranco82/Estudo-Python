#upper() -> não tem parâmetros
texto = 'eduardo'
texto = texto.upper()
print(texto)

#sort() -> apenas parâmetros keyword
lista = [1,2,3,7,6,5]
lista.sort(reverse=True)# esse parametro tem 1 unico key word reverse
print(lista)


#extend(lista) -> 1 parâmetro obrigatório

vendas_ano = [100, 200, 50, 90, 240, 300, 55, 10, 789, 60]
vendas_novdez = [500, 1555]

vendas_ano.extend(vendas_novdez)


#nossa função eh_da_categoria(bebida, cod_categoria) -> 2 parâmetros de posição obrigatórios