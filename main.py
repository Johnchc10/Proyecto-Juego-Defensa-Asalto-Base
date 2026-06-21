from modelos.mapa import Mapa
from modelos.unidad import Soldado
from modelos.muro import Muro

mapa = Mapa()

soldado = Soldado()
muro = Muro()

mapa.colocar_objeto(2, 0, soldado)
mapa.colocar_objeto(2, 1, muro)

print("Antes")
mapa.mostrar()

soldado.mover(mapa)

print("\nVida muro:")
print(muro.vida)