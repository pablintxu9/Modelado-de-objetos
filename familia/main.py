from familia.kate import kate
from familia.guillermo import guillermo
from familia.persona import persona
class familia:
    def __init__(self):
        self.personas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)

    def __str__(self):
        return f"Familia con {len(self.personas)} personas: " + ", ".join(str(p) for p in self.personas)
    
