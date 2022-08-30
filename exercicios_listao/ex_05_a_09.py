

# 5) Resolva estes problemas em Python, guardando os valores e seus resultados em
# variáveis diferentes.

# a. Calcule a área de um quadrado cujo lado seja 2 cm.
lado = 2
area = lado ** lado 
print(area)
# b. Uma mala custa R$120,00. Esta recebeu 5% de desconto. Quanto você irá pagar
# por ela.
mala = 120.00
desconto = 120.00 * 0.05
valor_final = mala - desconto
print(valor_final)

# c. Um carro está viajando a uma velocidade média de 100 Km/h, o trecho de viagem
# será 200 Km. Quantas horas irá demorar a viagem.

hora = 1
velocidade = 100 / hora
distancia = 200
tempo = distancia / velocidade
print(tempo)

# d. João tem 2 pirulitos, Maria 3 pirulitos e Sofia 1 pirulito. Calcule o total de pirulitos e
# sua média.
joao = 2
maria = 3
sofia = 1
total = joao + maria + sofia
media = total / 3
print(total, media)

# e. Davi tem 13 anos e sua irmã tem 7 anos. Guarde na variável eh_mais_velho a
# verificação se a idade de Davi é maior que a idade de sua irmã.

davi = 13
irma = 7

eh_mais_velho = davi > irma

print(eh_mais_velho)


# 6) Qual será o valor de z? Qual seria outra forma de escrever este trecho de código?
# z = 3
# z += 2
# z *= 6
# z /= 5

z = 3
#z += 2 
z= z + 2
#z *= 6
z = z * 6
#z /= 5
z = z / 5
print(z)


# 7) Considere as seguintes variáveis:
ovo = 3.4
caju = 12.4

# Qual será o valor de resposta em cada linha:
# resposta = ovo if 1 > 2 else caju
resposta_1 = ovo if 1 > 2 else caju
print(resposta_1)

# resposta = ovo if ovo > caju else caju
resposta_2 = ovo if ovo > caju else caju
print(resposta_2)

# resposta = ovo if ovo < caju else caju
resposta_3 = ovo if ovo < caju else caju
print(resposta_3)

# resposta = 100 if ovo + caju > 15 else 200
resposta_4 = 100 if ovo + caju > 15 else 200
print(resposta_4)

# resposta = 100 if ovo == 3 else 0
resposta_5 = 100 if ovo == 3 else 0
print(resposta_5)

# 8) Qual é o resultado deste problema? Qual é o valor final da variável fim?
ab = 10
Ab = 20
aB = 30
AB = ab + Ab - aB
fim = AB + 1

print(fim)

# 9) Qual é o resultado de cada linha de comando do Python? Siga a ordem dos comandos.

valor = input("Informe um valor: ")
print("Valor informado: ", valor)
tipo = type(valor)
print(tipo)

x_str = "123"
x = int(x_str)
xf = float(x)
sao_iguais = x == xf
print("Um float é igual a um int?", sao_iguais)


