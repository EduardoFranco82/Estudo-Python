def descobrir_servidor(email):
    try:
        posicao_a = email.index('@')
        print(posicao_a)
    except:
        raise ValueError('Email digitado não tem @, digite novamente')#usa o raise para exibir o erro e tambbem exibir uma msg personalizada
                                                                        #pq o ideal quando encontra um erro, e parar o programa e nao printar alguma coisa
   
        '''
        muda o tipo de aviso
        raise: TypeError
        raise: ValueError
        raise: ZeroDivisionError'''
        
   
    else:
        servidor = email[posicao_a:]
        print(servidor)
        if 'gmail' in servidor:
            return 'gmail'
        elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
            return 'hotmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        elif 'uol' in servidor or 'bol' in servidor:
            return 'uol'
        else:
            return 'não determinado'

email = descobrir_servidor('edu@gmail.com')
print(email)

#SOBRE EXCEÇOES
'''https://docs.python.org/3/library/exceptions.html'''

# Tipos de Erros e Exceções
# O Python tem inúmeros erros e exceções já prontas dentro dele, a lista completa está em: https://docs.python.org/3/library/exceptions.html
# Principais Erros/Exceções
# Vamos listar aqui alguns dos principais e que mais encontraremos, mas a lista completa está no link

# 1. ZeroDivisionError
# Quando tentamos dividir um número por zero

# 2. IndexError ou KeyError
# Quando tentamos pegar um índice que não existe em uma lista ou uma chave que não existe em um dicionário

# 3. TypeError ou AttributeError
# Quando tentamos atribuir um parâmetro para uma função que não tem parâmetros ou que não possui aquele parâmetro específico ou algum outro erro no parâmetro passado para a função

# 4. ImportError ou ModuleNotFoundError
# Quando tentamos importar um módulo não instalado no nosso computador ou algum objeto/função de um módulo que não existe

# 5. NameError
# Quando tentamos usar uma variável que não existe/não foi iniciada

# 6. SyntaxError
# Quando fizemos algum erro de escrita no código (deixamos de fechar algum parênteses, colchete ou chaves), escrevemos algo que não pode ser escrito ou escrevemos de forma errada

# 7. IndentationError ou TabError
# Quando damos mais ou menos vezes Tab do que deveria em alguma linha de código (mais ou menos indentação)

# 8. TypeError
# Quando tentamos fazer uma operação com um tipo de variável que não pode ser feito nela, ex: tentamos pegar o índice de um item de uma variável que é inteiro (ao invés de uma lista). Como números inteiros não são listas, teremos um typeerror

# 9. UnicodeError
# Quando o programa não conseguiu usar o método de encoding correto. Normalmente isso sinaliza a existência de algum caractere especial como ~, ç, etc. que está atrapalhando o código.

# 10. ValueError
# Quando passamos um valor que não pode ser passado para uma função ou método.