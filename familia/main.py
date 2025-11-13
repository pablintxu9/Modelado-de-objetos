from kate import kate
from guillermo import guillermo
from carlos import carlos
from diana import diana

# Relaciones
kate.casar_con(guillermo)
carlos.casar_con(diana)
guillermo.agregar_padres(carlos, diana)

# Mostrar toda la información
for persona in [kate, guillermo, carlos, diana]:
    persona.mostrar_info()
