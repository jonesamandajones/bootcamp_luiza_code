


# 22). Crie um script que leia 10 números inteiros positivos e que irá apresentar:
# ● A lista dos valores lidos de forma ordenada.
# ● A contagem de cada item. Por exemplo, se o usuário informou [1,1,1,1,2, 3],
# aqui apresentamos:
# ○ 1: 4x.
# ○ 2: 1x.
# ○ 3: 1x.
# ● Uma saída identificando o número, se o número é par e se é primo. Isto será feito
# separando por vírgulas: Por exemplo, se informou [1,2,3,6]. Iremos apresentar aqui:
# ○ 1,ímpar,não é primo
# ○ 2,par,é primo
# ○ 3,ímpar,é primo
# ○ 6,par,não é primo


numeros = []

entrada = int(input('Digite um número inteiro positivo:   '))

while len(numeros) <= 10:
    entrada = (int(input('Mais um número inteiro positivo, por favor:   ')))
    numeros.append(entrada) 
    if len(numeros) > 10:
        break
    

#1
numeros.sort()

#2
# 
def numeros_par(numeros_set):
    for n in numeros_set:
        if n%2 == 0:
            return 'é par'
        else:
            return 'é ímpar'
       

def numeros_primos(numeros_set):
    for n in numeros_set:
        if n%2 != 0 or n == 2 and not n == 9:
            return 'é primo'
        else:
            return 'não é primo'
        
        
def number_of_numbers(numeros):
    numeros_set = list(set(numeros))
    for n in numeros_set:
        contagem = numeros.count(n)
        print(f'{n}: {contagem}x. {numeros_par(numeros_set)}, {numeros_primos(numeros_set)}')
    return numeros_set

number_of_numbers(numeros)


        

            

