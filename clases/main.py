from clases.circulo import Circulo
from clases.rectangulo import Rectangulo
from clases.cuadrado import Cuadrado
from clases.elipse import Elipse


if __name__ == "__main__":
	c = Circulo("negro",1)         
	r = Rectangulo ("naranja",3, 1)    
	q = Cuadrado("azul", 1.5)        
	e = Elipse( "amarillo", 1, 3)    

	print(c)
	print(r)
	print(q)
	print(e)
