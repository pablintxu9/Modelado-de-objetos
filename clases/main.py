from clases.circulo import Circulo
from clases.rectangulo import Rectangulo
from clases.cuadrado import Cuadrado
from clases.elipse import Elipse


if __name__ == "__main__":
	c = Circulo(1,"negro")         
	r = Rectangulo(3, 1, "naranja")    
	q = Cuadrado(1.5, "azul")        
	e = Elipse(1, 3, "amarillo")    

	print(c)
	print(r)
	print(q)
	print(e)
