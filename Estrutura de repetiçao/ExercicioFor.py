'''Criando um Registro de Hóspedes
Digamos que você está criando o sistema para registrar a chegada de hóspedes em um hotel. No hotel, os hóspedes podem ter quartos com 1, 2, 3 e 4 pessoas. Seu sistema deve conseguir:

Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto (perguntando por meio de input)
De acordo com a quantidade de pessoas do hóspede, ele deve fazer um for para perguntar o cpf e o nome de cada pessoa, a fim de registrá-la no quarto (2 inputs para cada pessoa, 1 para o cpf e outro para o nome)
O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que cada item dessa lista é o nome da pessoa e o cpf da pessoa, assim:'''

#input recebe sempre uma string

qtdade_pessoas = int(input('Digite a quantidade de pessoas'))
quarto = []

for i in range(qtdade_pessoas):
    cpf = input('digite seu cpf pessoa {}'.format(i + 1))
    nome = input('digite seu nome')
    hospede = ['nome : {} cpf: {}'.format(nome, cpf)]
    quarto.append(hospede)

print(quarto)


#Analise de vendas
# Temos uma lista com os vendedores e os valores de vendas e quermos identificar
# quais os vendedores que bateram a meta e qual foi o valor que eles venderam

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
#seu código aqui
for item in vendas:
    if item[1] >= meta:
        print ('o vendedor {} bateu a meta com o valor de {}'.format(item[0], item[1]))