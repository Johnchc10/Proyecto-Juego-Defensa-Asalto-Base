from modelos.mapa import Mapa
from modelos.partida import Partida

partida = Partida()
mapa = Mapa()

mapa.base.recibir_daño(1000)

partida.verificar_ganador_ronda(mapa)

print(partida.victorias_atacante)