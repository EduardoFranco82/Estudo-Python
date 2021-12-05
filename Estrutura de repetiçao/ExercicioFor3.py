'''Faremos algo parecido com "filtrar" uma lista. Mais pra frente no curso aprenderemos outras formas de fazer isso, mas com o nosso conhecimentoa atual já conseguimos resolver o desafio.

Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, eu quero conseguir calcular o % de vendedores que bateram a meta. Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta.'''

acima_meta = []
meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
for venda in vendas:
    if venda[1] > meta:
        acima_meta.append(venda)

print(acima_meta)
print(' a porcentagem de vendedores acima da media e {:.1%}'.format(len(acima_meta)/len(vendas)))


#forma diferente
quantidade_vendedores_acima = 0

for venda in vendas:
    if venda[1] >= meta:
        quantidade_vendedores_acima += 1
print('a porcentagem de vendedores que bateram a meta {:.1%}'.format(quantidade_vendedores_acima/len(vendas)))


#outra forma

melhor_vendedor = ''
maior_vendas = 0

for venda in vendas:
    if venda[1] > maior_vendas:
        maior_vendas = venda[1]
        melhor_vendedor = venda[0]
        
print('O melhor vendedor foi {} com {} vendas'.format(melhor_vendedor, maior_vendas))