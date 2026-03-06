from backend import *
from frontend import *

usuario1=Usuario("Gael",23,"Croquetas de atun")
usuario2=Usuario("Dana",19,"lassagna")
usuario3=Usuario("Camy",18,"Tacos")

print(usuario1.mostrar_datos())
print(usuario2.mostrar_datos())
print(usuario3.mostrar_datos())

print(Usuario.mostrar_lista())