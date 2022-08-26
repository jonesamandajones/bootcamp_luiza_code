# 1l > 3m²
#18l > R$80,00

# 18 / 80 = 0.225
#3m² = 0.225

#18**
import math
print('Seja muito bem-vindo à nossa loja de tintas ~COMO EU PINTO~! \n Aqui você encontra um só valor de tinta para todas as nossas opções! \n Cada uma de nossas latas de tinta tem o total de 18L, e cada litro dela pinta até 3m²! \n E você tá se perguntando quanto custa tal maravilha? APENAS R$80,00 A LATA!!! APROVEITE!')


area_pintar = int(input('Informe qual o tamanho em m² da superfície a ser pintada ')) 

LITRO_PINTA = 3
VOLUME_LATA = 18
LATA_PINTA = LITRO_PINTA * VOLUME_LATA

numero_latas = math.ceil(area_pintar / LATA_PINTA)

valor = numero_latas * 80.00

print(f'Você precisará de {numero_latas} latas de tinta, que resulta em apenas R$ {valor}! Aceitamos todos os cartões!')









