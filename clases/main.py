from clases.circulo import Circulo
from clases.rectangulo import Rectangulo
from clases.cuadrado import Cuadrado
from clases.elipse import Elipse


def main():
	# Generar un círculo y imprimirlo (color por defecto: 'negro')
	c = Circulo(1,"negro")           # Circulo: color por defecto 'negro'
	r = Rectangulo(3, 1, "naranja")    # Rectangulo: color por defecto 'naranja'
	q = Cuadrado(1.5, "azul")         # Cuadrado: color por defecto 'azul'
	e = Elipse(1, 3, "amarillo")        # Elipse: color por defecto 'amarillo'

	print(c)
	print(r)
	print(q)
	print(e)
