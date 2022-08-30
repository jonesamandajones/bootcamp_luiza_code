

# 14) Crie o seguinte programa Python no arquivo ex14.py: Colete a idade de duas pessoas.
# E informe se a primeira idade é maior do que a da primeira. Neste aqui, basta responder
# True para informar que a primeira idade é maior que a primeira.

idade_1 = int(input('Olá, pessoa! Qual a sua idade?   '))
idade_2 = int(input('E a idade da sua mãe quando você nasceu?   '))
resposta = idade_1 < idade_2

print(f'Você é mais novo que sua mãe quando ela te teve? {resposta}')

