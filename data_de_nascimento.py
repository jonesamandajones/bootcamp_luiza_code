


data = input('Olá! Informe sua data de nascimento no formato 00/00/0000:       ')

print(f"Obrigada! Segundo suas informações, você nasceu no dia {data.split('/')[0]} do mês {data.split('/')[1]} no ano de {data.split('/')[2]}")

dia, mes, ano = data.split('/')
