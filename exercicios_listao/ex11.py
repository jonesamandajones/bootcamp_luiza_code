

# 11) Programa Python no arquivo ex11.py: Este programa irá calcular a área de um
# quadrado. Peça para a pessoa informar a medida numérica de um lado do quadrado. E
# depois informe-lhe o valor da área do quadrado.

lado = int(input('''Olá pessoa! Para calcular o valor da área de um quadrado é preciso saber o comprimento de seus lados.
                 Por favor, informe aqui, em centímetros, o tamanho do lado de seu quadrado:    '''))
area = lado * lado

print(f'Tendo {lado}cm de comprimento em cada lado, o quadrado tem {area}cm² de área. Pode confiar. ;)')

