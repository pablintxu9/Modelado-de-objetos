class obras:
    def __init__(self, titulo, año, tecnica, subtecnica, soporte, autor, estado):
        self.titulo = titulo
        self.año = año
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.autor = autor
        self.estado = estado
    def asignar_lugar(self, lugar):
        self.lugar=lugar
    def __str__(self):
        
