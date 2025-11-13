from clases.figuras import Figura

class Circulo(Figura):
    def __init__(self, radio, color):
        self.radio = radio
        super().__init__(color)

    def __str__(self):
        return f'Circulo(Radio: {self.radio}, Color: {self.color})'