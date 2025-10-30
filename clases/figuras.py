class Figura:
    def __init__(self):
        self.figuras = []

    def __str__(self):
        # Representación genérica de una figura: nombre de la clase y atributos públicos
        attrs = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        return f"{self.__class__.__name__}({', '.join(f'{k}: {v}' for k, v in attrs.items())})"

