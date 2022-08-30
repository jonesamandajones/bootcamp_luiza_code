


from curses import wrapper


def decorator(funcao):
    def wrapper():
        print ('primeira string!')
        função()
        print('Segunda string!')
    return wrapper

def outra_funcao():
    print ('Um belo argumento!')

funcao_decorada = decorator(outra_funcao)
funcao_decorada()


#DECORATOOOOOOR!!!



