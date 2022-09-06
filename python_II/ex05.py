


# 5. Escreva uma classe “Quadrado”, crie dois métodos que retornem a
# área do quadrado e o perímetro, não crie a instância nesse exercício.


class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        
    def area_quadrado(self):
        area = self.lado * self.lado
        return f'A área do quadrado mede {area}cm.'
    
    def perimetro(self):
        perimetro = self.lado * 4
        return f'O perímetro do quadrado mede {perimetro}cm.'
        
        
        