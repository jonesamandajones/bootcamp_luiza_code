


primeira_nota = int(input('Qual a nota da sua primeira avaliação?   '))

segunda_nota = int(input('Qual a nota da sua segunda avaliação?   '))

media = (primeira_nota + segunda_nota) / 2

if media == 10 :
    print('Aprovadíssimo!')
elif media <= 9 and media >= 7 :
    print('Aprovado!')
else:
    print('Reprovado')
    
    
        
    