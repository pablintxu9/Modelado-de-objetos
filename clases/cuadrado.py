from clases.figuras import Figura

class Cuadrado(Figura):
    def __init__(self, lado, color):
        self.lado = lado
        super().__init__(color) 

    def __str__(self):
        return f'Cuadrado(Lado: {self.lado}, Color: {self.color})'