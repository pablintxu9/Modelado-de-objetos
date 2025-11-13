class Persona:
    def __init__(self, nombre, apellido, sexo, apellido_nacimiento=None):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido_nacimiento = apellido_nacimiento
        self.sexo = sexo
        self.conyuge = None
        self.padres = []

    def casar_con(self, otra_persona):
        self.conyuge = otra_persona
        otra_persona.conyuge = self

    def agregar_padres(self, padre, madre):
        self.padres = [padre, madre]

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        if self.apellido_nacimiento:
            print(f"Apellido de nacimiento: {self.apellido_nacimiento}")
        print(f"Sexo: {self.sexo}")
        if self.conyuge:
            print(f"Está casado con: {self.conyuge.nombre}")
        if self.padres:
            print(f"Hijo de: {self.padres[0].nombre} y {self.padres[1].nombre}")
        print("-" * 30)
