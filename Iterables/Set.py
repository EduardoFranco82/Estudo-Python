'''Set
Estrutura:
meu_set = {valor, valor, valor, valor,...}

Observações:
Não pode ter valores duplicados
Não tem ordem fixa'''

#SET NAO E DICIONARIO CHAVE VALOR, ATENÇAO PARA ISSO
#SET E PARA CONTAGEM DE VALORES UNICOS, E NAO GUARDA POSIÇAO

#set_produtos = {} # ta errado, isso e um dicionario
set_produtos = {'arroz', 'arroz', 'feijao', 'macarrao', 'atum', 'azeite'} #maneira certa

print(set_produtos)


cpf_clientes = ['762.196.080-97', '263.027.380-67', '827.363.930-40', '925.413.640-91', '870.565.160-33', '892.080.930-50', '462.126.030-81', '393.462.330-10', '393.462.330-10', '393.462.330-10', '988.305.810-11', '596.125.830-05', '596.125.830-05', '990.236.770-48']
print(len (cpf_clientes))

set_cpf_clientes = set(cpf_clientes)
print(len(set_cpf_clientes))

cpf_clientes_unicos = list(set_cpf_clientes)
print (cpf_clientes_unicos)