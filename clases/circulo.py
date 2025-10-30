from clases.figuras import Figura

class Circulo(Figura):
    def __init__(self, radio, color):
        super().__init__()
        self.radio = radio
        self.color = color

    def __str__(self):
        return f'Circulo(Radio: {self.radio}, Color: {self.color})'