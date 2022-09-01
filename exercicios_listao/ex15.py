


# 15). Para o programa Python no arquivo ex15.py: Em uma casa, uma família decidiu dividir
# o valor da conta de energia entre os moradores da casa. No programa eles informam o
# valor da conta de energia e quantos que irão pagar a conta no mês. O programa calculará
# quanto cada um deverá contribuir com a conta de energia.

conta = float(input(' Informe o valor da conta de energia deste mês:   '))
familiares = float(input('Informe o número de familiares moradores da casa neste mês:   '))

cada_um = conta / familiares

print(f'O valor da conta de energia deste mês será de R${cada_um} para cada familiar.')

