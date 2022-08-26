

first = int(input('Give me a number:    '))
second = int(input('Give me another number:  '))
third = int(input('Now give me one more number: '))
fourth = int(input('You aready know, I want another number?  '))
fifth = int(input("I swear, I'll don't ask this anymore after this time, give me the last number, please:    "))

lista = [first, second, third, fourth, fifth]

# lista.sort()

zero = lista[0]
um = lista[1]
dois = lista[2]
tres = lista[3]
quatro = lista[4]

lista_ord = []
for n in range(5):
    if n == 4:
        break
    if lista[n] < lista[n+1]:
       lista_ord.append(lista[n])
    else: 
        lista_ord.append(lista[n+1]) 

print(lista)
print(lista_ord)

    
    

    








# print(f'Here are all your answers, but organized: \n {lista}')


      