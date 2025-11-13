from familia.persona import persona
class guillermo(persona):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Guillermo: {self.nombre}, Edad: {self.edad}"