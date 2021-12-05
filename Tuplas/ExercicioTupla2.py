'''Temos uma lista com os vendedores e os valores de vendas e queremos identificar
 (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam.'''

meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]

for nome,venda in vendas:
    if venda > meta:
        print('o vendedor foi {} e o valor foi {}'.format(nome, venda))
