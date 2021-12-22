'''Range
Estrutura:
range(tamanho)
ou

range(inicio, fim)
ou

range(inicio, fim, passo)'''

#uso mais comum no for:
produtos = ['arroz', 'feijao', 'macarrao', 'atum', 'azeite']
estoque = [50, 100, 20, 5, 80]

for i in range(5):
    print('{}: {} em estoque'.format(produtos[i], estoque[i]))



#range com inicio e fim
print(range(1, 10))

#vamos olhar no for para entender
for i in range(2, 10):# vai printar ate o 9, sempre é 1 a menos
    print(i)