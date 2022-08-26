from functools import reduce

def foo(value):
    print(f'Olá, esse é o parametro: {value}')
    
foo('LuizaCode')
    
lista = [100, 248.90, 88, 124.90]

def desconto(preco):
    return preco * (1 -0.1)

# 1-Dada uma lista com n valores, aplicar a função de desconto usando map()
lista_desconto = map(lambda x: desconto(x), lista)

print(list(lista_desconto))

# 2-Retornar os valores maiores q 100, usando filter()
maior_100 = filter(lambda x: x > 100, lista)

print(list(maior_100))
 
# 3-Somar todos os valores da lista usando reduce()
soma_total = reduce(lambda x, y: x+y, lista)

print(soma_total)