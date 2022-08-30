

# 12) Programa Python no arquivo ex12.py: Este programa irá calcular a área de um
# triângulo. Peça para a pessoa informar a medida numérica da base do triângulo, depois
# colete o valor da altura. Apresente o valor da área do triângulo.

base = int(input('Olá! Por favor, informe em cm, o comprimento da base do triângulo que você deseja calcular a área:   '))
altura = int(input('Agora informe também a medida em cm da altura do triângulo:   '))
area = (base * altura) / 2

print(f'Muito bem! O valor da área do  seu triângulo é {area}cm²!')
                



# 14) Crie o seguinte programa Python no arquivo ex14.py: Colete a idade de duas pessoas.
# E informe se a primeira idade é maior do que a da primeira. Neste aqui, basta responder
# True para informar que a primeira idade é maior que a primeira.
# 15). Para o programa Python no arquivo ex15.py: Em uma casa, uma família decidiu dividir
# o valor da conta de energia entre os moradores da casa. No programa eles informam o
# valor da conta de energia e quantos que irão pagar a conta no mês. O programa calculará
# quanto cada um deverá contribuir com a conta de energia.
# 16). Programa ex16.py: Estou tentando entender os juros do meu banco. Para isto, ele me
# informou esta fórmula:
# valor_final = valor_emprestimo + (valor_emprestimo * taxa * tempo)
# onde que:
# ● valor_emprestimo: É o valor que pegarei emprestado.
# ● taxa: É o valor da taxa por mês. Por exemplo: se for 4% ao mês, o valor será 0.04.
# ● tempo: Quantidade de meses que irei pagar o empréstimo.
# Crie um programa que colete cada um destes valores para calcular o valor final que estarei
# pagando ao banco.
# 17) Desafio ex17.py: Dada uma equação de segundo grau, calcule suas raízes utilizando a
# fórmula de Bhaskara.
# 18) Faça um programa que leia a nota de um aluno. Garanta que a nota seja um
# valor inteiro entre zero e 100. Se o valor não estiver neste intervalo, informe que a
# nota é inválida. Se a nota for maior que 60, informa que o aluno foi aprovado; caso
# contrário, informa que ele foi reprovado.
# 19). Um vendedor ganha uma comissão de uma venda da seguinte forma: Se a
# venda for …
# ● menor que R$1000,00, o vendedor não ganha nenhuma comissão;
# ● entre R$1.000,00 e R$5.000,00, o vendedor ganha uma comissão de 10% da
# venda;
# ● entre R$5.000,00 e R$10.000,00, a comissão será de 20% da venda;
# ● entre R$10.000,00 e R$50.000,00 a comissão será de 25% da venda;
# ● acima de R$50.000,00 a comissão será de 30% da venda.
# Faça um programa que informe o valor da comissão do vendedor para uma venda.
# 20) Crie um programa para calcular o valor a ser pago para um determinado produto para a
# empresa NaoQueroMuitoSeuDinheiro. O pessoal desta empresa pediu o seguinte:
# ● Vamos coletar três valores:
# ○ O valor inicial da parcela.
# ○ O valor percentual de cada parcela.
# ○ A quantidade de parcelas.
# ● Para cada parcela a ser paga, o cálculo é o seguinte:
# valor_parcela = valor_anterior + (valor_anterior *
# percentual)
# ● No caso da primeira parcela, o valor anterior é o valor inicial.
# Crie um programa que irá mostrar cada parcela e o seu valor. Por exemplo: se o valor inicial
# for $100,00, o valor do percentual for 0,10, e a quantidade de parcelas for 2; logo nosso
# programa irá mostrar:
# Parcela 1: $ 110.0
# Parcela 2: $ 121.0
# 21. O pessoal da empresa Caça-Clientes trabalha com ligações para números aleatórios.
# Eles recebem uma lista com vários intervalos de números para eles ligarem. Na lista
# recebida, você tem o prefixo do telefone, o primeiro sufixo e o último sufixo. Crie um script
# que liste todos os números dos telefones, ao serem informados, o prefixo e os sufixos. Por
# exemplo, suponha que o prefixo seja “3232” e que o primeiro prefixo seja “0001” e o último
# sufixo seja “0005”; logo o programa irá imprimir:
# Seus números de telefone são:
# ● 3232-0001
# ● 3232-0002
# ● 3232-0003
# ● 3232-0004
# ● 3232-0005
# 22). Crie um script que leia 10 números inteiros positivos e que irá apresentar:
# ● A lista dos valores lidos de forma ordenada.
# ● A contagem de cada item. Por exemplo, se o usuário informou [1,1,1,1,2, 3],
# aqui apresentamos:
# ○ 1: 4x.
# ○ 2: 1x.
# ○ 3: 1x.
# ● Uma saída identificando o número, se o número é par e se é primo. Isto será feito
# separando por vírgulas: Por exemplo, se informou [1,2,3,6]. Iremos apresentar aqui:
# ○ 1,ímpar,não é primo
# ○ 2,par,é primo
# ○ 3,ímpar,é primo
# ○ 6,par,não é primo
# 23) Neste script você irá ler o nome de 4 alunos e suas notas e determinar qual
# aluno possui a maior nota.