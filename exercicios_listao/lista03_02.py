 
 
 
 #10) Crie o seguinte programa Python no arquivo lista03_02.py: Colete o nome da
# pessoa, a cidade de nascimento dela, e o ano em que ela nasceu. Depois você irá mostrar
# os dados coletados em linhas diferentes. E também, deverá informar quantos anos a
# pessoa terá no ano 2030.

nome = input('Olá!, por favor, informe o seu nome:   ')
cidade = input('Agora informe o nome da cidade em que você nasceu:   ')
ano = int(input('Para finalizar, digite o ano do seu nascimento:   '))
futuro = 2030 - ano

print( f'''Olá, {nome}! 
    Você nasceu em {cidade}.
    No ano de {ano}.
    Em 2030, você fará {futuro} anos! Obrigada, de nada! :D''')

