from modelos.jugador import Jugador
from modelos.partida import Partida
from modelos.mapa import Mapa

defensor = Jugador.iniciar_sesion(
    "John",
    "1234"
)

atacante = Jugador.iniciar_sesion(
    "Pedro",
    "456"
)

partida = Partida()
mapa = Mapa()

resultado = partida.verificar_ganador_ronda(
    mapa,
    defensor,
    atacante
)

print(resultado)