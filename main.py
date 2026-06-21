from modelos.mapa import Mapa
from modelos.muro import Muro
from modelos.torre import TorreArquero
from modelos.unidad import Soldado

from interfaz.tablero import Tablero

mapa = Mapa()

mapa.colocar_objeto(4, 5, Muro())
mapa.colocar_objeto(5, 4, TorreArquero())
mapa.colocar_objeto(2, 2, Soldado())

Tablero(mapa)