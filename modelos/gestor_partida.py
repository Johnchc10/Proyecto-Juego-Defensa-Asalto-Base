class GestorPartida:

    def __init__(self):

        self.jugador1 = None
        self.jugador2 = None

        self.defensor = None
        self.atacante = None

        self.faccion_defensor = None
        self.faccion_atacante = None
    
    def asignar_jugadores(
        self,
        jugador1,
        jugador2
    ):

        self.jugador1 = jugador1
        self.jugador2 = jugador2
    
    def asignar_roles(
        self,
        defensor,
        atacante
    ):

        self.defensor = defensor
        self.atacante = atacante
    
    def asignar_facciones(
        self,
        faccion_defensor,
        faccion_atacante
    ):

        self.faccion_defensor = faccion_defensor
        self.faccion_atacante = faccion_atacante