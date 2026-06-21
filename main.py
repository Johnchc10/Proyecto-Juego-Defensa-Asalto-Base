from modelos.jugador import Jugador
from modelos.gestor_partida import GestorPartida

from interfaz.roles import Roles
from interfaz.facciones import Facciones

gestor = GestorPartida()

j1 = Jugador("John", "123")
j2 = Jugador("Pedro", "456")

gestor.asignar_jugadores(
    j1,
    j2
)

roles = Roles(j1, j2)

gestor.asignar_roles(
    roles.obtener_defensor(),
    roles.obtener_atacante()
)

facciones = Facciones()

gestor.asignar_facciones(
    facciones.obtener_faccion_defensor(),
    facciones.obtener_faccion_atacante()
)

print("Defensor:", gestor.defensor.usuario)
print("Atacante:", gestor.atacante.usuario)

print("Facción defensor:", gestor.faccion_defensor)
print("Facción atacante:", gestor.faccion_atacante)