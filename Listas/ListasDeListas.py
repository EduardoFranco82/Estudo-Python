vendedores = ['Lira', 'João', 'Diego', 'Alon']
produtos = ['ipad', 'iphone']
vendas = [
    [100, 200],
    [300, 500],
    [50, 1000],
    [900, 10],
]


vendasIpadJoao = vendas[1] [0]
print (vendasIpadJoao)

vendas_iphone = vendas[0] [1] + vendas[1] [1] + vendas[2] [1] +vendas[3] [1]

print(vendas_iphone)


#modificando
# Lira fez apenas 50 vendas de iphne

vendas[0][1] = 50
print(vendas)