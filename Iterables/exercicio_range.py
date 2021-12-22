'''Exemplo: Modelo Jack Welch da G&E

Classe A: 10% melhor
Classe B: 80% mantém/busca melhorar
Classe C: 10% pior
Quem são os funcionários classe B?'''



funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo']
vendas = [2750, 1900, 1500, 1200, 1111, 1100, 999, 900, 880, 870, 800, 800, 450, 400, 300, 300, 120, 90, 80, 70]


for i in range (2,18):
    print ('{} vendeu: {}'.format(funcionarios[i], vendas[i]))



#range com passo
print(range(0, 1000, 10))#pula de 10 em 10

for i in range(0, 1000, 10):
    print(i)