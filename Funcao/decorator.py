#decorator '@' muda o comportamento de uma funçao existente, adicionando outro comportamento nela
#de uma outra funçao existente



class maiusculo (object):
    def __init__(self,f) :
        print('funcionalidade de deixar maiusculo')
        self.f = f

    def __call__(self, *args):
        self.f(args[0].upper())




@maiusculo
def printar_nome(nome):
   # colocar_maiusculo = nome.upper() ao invers disso vou usar um decorator, que ja faz um texto ficar em maiusculo
   # print(colocar_maiusculo)
    print(nome)
printar_nome('maria')