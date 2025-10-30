from clases.figuras import Figura

class Cuadrado(Figura):
    def __init__(self, lado, color):
        super().__init__()
        self.lado = lado
        self.color = color

    def __str__(self):
        return f'Cuadrado(Lado: {self.lado}, Color: {self.color})'