from clases.circulo import Circulo
from clases.rectangulo import Rectangulo
from clases.cuadrado import Cuadrado
from clases.elipse import Elipse


def main():
	# Generar un círculo y imprimirlo (color por defecto: 'negro')
	c = Circulo(5)           # Circulo: color por defecto 'negro'
	r = Rectangulo(3, 1)    # Rectangulo: color por defecto 'naranja'
	q = Cuadrado(1.5)         # Cuadrado: color por defecto 'azul'
	e = Elipse(1, 3)        # Elipse: color por defecto 'amarillo'

	print(c)
	print(r)
	print(q)
	print(e)


if __name__ == '__main__':
	main()
