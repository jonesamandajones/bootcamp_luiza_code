


# 17) Desafio ex17.py: Dada uma equação de segundo grau, calcule suas raízes utilizando a
# fórmula de Bhaskara.

a = int(input('Informe o valor de "a":   '))
b = int(input('Informe o valor de "b":   '))
c = int(input('Informe o valor de "c":   '))

delta = b**2 - 4 * a * c

x = (- b + delta ** (1/2)) / (2 * a)
x2 = (- b - delta ** (1/2)) / (2 * a)

print(x)
print(x2)

