# sempre que vai trabalhar com datas
#sempre existe uma data que e marco 0

import time
#unidade de tempo para modulo time em python é segundos
# marco zero 1/1/70 00:00:00

#time() retorna quantos segundos se passaram desde a hora de marco 0
segundos_ate_hoje = time.time()
print(segundos_ate_hoje)

#ctime() retorna um texto com a data de hoje

data_de_hoje = time.ctime()
print(data_de_hoje)


tempo_inicial = time.time()
for i in range(100000000):
    pass
tempo_final = time.time()
duracao = tempo_final - tempo_inicial
print(duracao)


def rodar5segundos():
    print('inicio')
    time.sleep(5)
    print ('depois de 5 segundo')

rodar5segundos()



#pegar informacao de minuto, segundo , hora, tudo detalhando

#gmtime()
#gmtime().parametro

data_atual = time.gmtime()
print(data_atual)


ano = data_atual.tm_year
mes = data_atual.tm_mon
dia = data_atual.tm_mday
hora = data_atual.tm_hour
dia_da_semana = data_atual.tm_wday

print('Hoje é dia {}/{}/{}'.format(dia, mes, ano))