#mesma coisa que lista, porem coloca-se entre parenteses
#parece uma lista, mas e imutavel
#vantagem, mais eficiente, protege a base de dados, muito usado para dados heterogeneos


#nao pode mudar os dados dela



vendas = ('Lira', '25/08/2020', '15/02/1994', 2000, 'Estagiário')
print(vendas)

#vendas[3] = 3000 # nao da pra fazer

nome = vendas[0]
data_contratacao = vendas[1]
data_nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]

#da pra fazer dfe forma diferente mais facil, e a ordem importa
nome, data_contratacao, data_nascimento, salario, cargo = vendas


print(cargo)

