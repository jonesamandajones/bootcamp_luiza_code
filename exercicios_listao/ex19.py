


# 19). Um vendedor ganha uma comissão de uma venda da seguinte forma: Se a
# venda for …
# ● menor que R$1000,00, o vendedor não ganha nenhuma comissão;
# ● entre R$1.000,00 e R$5.000,00, o vendedor ganha uma comissão de 10% da
# venda;
# ● entre R$5.000,00 e R$10.000,00, a comissão será de 20% da venda;
# ● entre R$10.000,00 e R$50.000,00 a comissão será de 25% da venda;
# ● acima de R$50.000,00 a comissão será de 30% da venda.
# Faça um programa que informe o valor da comissão do vendedor para uma venda.

venda = float(input('Valor da venda em reais R$:   '))

if venda <= 1000:
    print('O vendedor não terá comissão.')
if venda > 1000 and venda <= 5000:
    print(f'O vendedor receberá 10%, no valor de R${venda * 0.1}.')
if venda > 5000 and venda <= 10000:
    print(f'O vendedor receberá 20%, no valor de R${venda * 0.2}.')
if venda > 10000 and venda <= 50000:
    print(f'O vendedor receberá 25%, no valor de R${venda * 0.25}.')
if venda > 50000:
    print(f'O vendedor receberá 30%, no valor de R${venda * 0.3}.')
          
