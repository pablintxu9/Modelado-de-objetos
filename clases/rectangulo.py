from clases.figuras import Figura

class Rectangulo(Figura):
    def __init__(self, ancho, alto, color):
        super().__init__(color)
        self.ancho = ancho
        self.alto = alto
    

    def __str__(self):
        return f'Rectangulo(Ancho: {self.ancho}, Alto: {self.alto}, Color: {self.color})'