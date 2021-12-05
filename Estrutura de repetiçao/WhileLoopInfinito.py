# registrar um produto e armazenar nujma lista, o programa para quando aperta o enter
# quando aperta o enter, recebe uma ''

venda = input('registre um produto, para cancelar aperte o enter')
vendas = []

while venda != '':
    vendas.append(venda)
    venda = input('registre um produto, para cancelar aperte o enter')

print('as vendas cadastradas foram{}'.format(vendas))


#Cuidado com loop infinito
vendas = [941, 852, 783, 714, 697, 686, 685, 670, 631, 453, 386, 371, 294, 269, 259, 218, 208, 163, 125, 102, 87, 47, 7]
vendedores = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']
meta = 50

i = 0
#problema, no while o i nao vai incrementando, entao virou infinito
while vendas[i] > meta:
    print('{} bateu a meta. Vendas: {}'.format(vendedores[i], vendas[i]))
    i += 1# resolve o problema