#while e laço de repetição

resposta = input('Bora dá um rolê [s/n]?    ')

n = 1

while resposta != 's':
    resposta = input(f'Bora{"a" * n} [s/n]??    ')
    n += 1
    if 'chato' in resposta or 'chata' in resposta:
        print('Foi mal!')
        break
else:
    print('Então bora{"a" * n}!!!')
    
