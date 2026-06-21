class Partida:
    def __init__(self):
        self.ronda = 1
        
        self.victorias_defensor = 0
        self.victorias_atacante = 0
        
    
    
    def verificar_ganador_ronda(
        self,
        mapa,
        defensor,
        atacante
    ):

        if mapa.base_destruida():

            self.victorias_atacante += 1
            atacante.sumar_victoria_atacante()
            print("Gana el atacante")

            return "atacante"

        if not mapa.quedan_unidades():

            self.victorias_defensor += 1
            defensor.sumar_victoria_defensor()
            print("Gana el defensor")

            return "defensor"

        return None
    
    def nueva_ronda(self, defensor, atacante):

        self.ronda += 1

        defensor.agregar_dinero(100)
        atacante.agregar_dinero(100)

        print(f"Comienza la ronda {self.ronda}")
    
    def partida_terminada(self):

        return (
            self.victorias_defensor >= 3
            or
            self.victorias_atacante >= 3
        )