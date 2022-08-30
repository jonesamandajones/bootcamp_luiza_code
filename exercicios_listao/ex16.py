

# 16). Programa ex16.py: Estou tentando entender os juros do meu banco. Para isto, ele me
# informou esta fórmula:
# valor_final = valor_emprestimo + (valor_emprestimo * taxa * tempo)
# onde que:
# ● valor_emprestimo: É o valor que pegarei emprestado.
# ● taxa: É o valor da taxa por mês. Por exemplo: se for 4% ao mês, o valor será 0.04.
# ● tempo: Quantidade de meses que irei pagar o empréstimo.
# Crie um programa que colete cada um destes valores para calcular o valor final que estarei
# pagando ao banco.]

from traceback import TracebackException


valor_emprestimo = float(input('Informe o valor total do empréstimo, em R$:   '))
taxa = float(input('Valor da taxa mensal em %:   ')) / 100
tempo = int(input('Quantidade de meses, ou parcelas:   '))

valor_final = valor_emprestimo + (valor_emprestimo * taxa * tempo)

print(f'O valor total a pagar ao banco será de R${valor_final}.')