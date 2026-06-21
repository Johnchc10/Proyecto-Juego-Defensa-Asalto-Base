class Partida:
    def __init__(self):
        self.ronda = 1
        
        self.victorias_defensor = 0
        self.victorias_atacante = 0
        
    def verificar_ganador_ronda(self, mapa):

        if mapa.base_destruida():

            self.victorias_atacante += 1

            print("Gana el atacante")

            return True

        return False
    
    def verificar_ganador_partida(self):

        if self.victorias_atacante >= 3:

            print("El atacante ganó la partida")

            return True

        if self.victorias_defensor >= 3:

            print("El defensor ganó la partida")

            return True

        return False