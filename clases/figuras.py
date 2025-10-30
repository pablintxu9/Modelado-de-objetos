class Figura:
    def __init__(self):
        self.figuras = []

    def agregar_figura(self, figura, color):
        self.figuras.append({'figura': figura, 'color': color})

    def mostrar_figuras(self):
        for item in self.figuras:
            print(f'Figura: {item['figura']}, Color: {item['color']}')
    
    def __str__(self):
        return '\n'.join([f'Figura: {item['figura']}, Color: {item['color']}' for item in self.figuras])
