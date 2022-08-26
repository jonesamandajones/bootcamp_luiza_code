

# receba uma string e responda se ela tem alguma vogal e quais são, e diga se é uma frase ou não.



resposta = input('Digite o que você quiser:')
espaço = ' '

if resposta.count('a') >= 1:
    print(resposta[resposta.find('a')]) 
if resposta.count('e') >= 1:
    print(resposta[resposta.find('e')]) 
if resposta.count('i') >= 1:
    print(resposta[resposta.find('i')]) 
if resposta.count('o') >= 1:
    print(resposta[resposta.find('o')]) 
if resposta.count('u') >= 1:
    print(resposta[resposta.find('u')]) 


if resposta.count('a') + resposta.count('e') + resposta.count('i') + resposta.count('o') + resposta.count('u') >= 1 :
   vogal = True
else:
    vogal = False

if  vogal == True and espaço in resposta:
    print('Você escreveu uma frase com vogais!')
    
   
