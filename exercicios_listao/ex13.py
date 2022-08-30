
# 13). Crie o seguinte programa Python no arquivo ex13.py: Colete a idade de 3 pessoas e
# mostre a média de suas idades.

idade_1 = int(input('''Olá três pessoas! Por favor, informe separadamente, a idade de cada um de vocês a seguir.
                     Idade da pessoa 1:   '''))
idade_2 = int(input('Agora a idade da pessoa 2:   '))
idade_3 = int(input('Para finalizar, informe a idade da pessoa 3:   ')) 
media = (idade_1 + idade_2 + idade_3) / 3

print(f'Obrigada! As idades são, respectivamente {idade_1},  {idade_2} e {idade_3}, sendo {media} a média de idade entre vocês! Obrigada, de nada!')


