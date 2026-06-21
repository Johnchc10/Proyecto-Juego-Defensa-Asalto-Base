from modelos.mapa import Mapa
from modelos.jugador import Jugador

from interfaz.tablero import Tablero

# Crear jugador de prueba
jugador = Jugador("John", "1234")

# Crear mapa
mapa = Mapa()

# Abrir tablero
Tablero(mapa, jugador)