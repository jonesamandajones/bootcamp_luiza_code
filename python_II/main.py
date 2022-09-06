
# 6. Crie um arquivo main.py, importe a classe “Quadrado”, crie uma nova
# instância e acesse seus métodos.

from ex05 import Quadrado

lado = float(input('Digite o comprimento do lado do quadrado em centímetros:    '))

quadrado = Quadrado(lado)
area = quadrado.area_quadrado()
perimetro = quadrado.perimetro()

print(area, perimetro)

