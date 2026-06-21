class Base:
    def __init__(self):
        self.vida = 1000
        self.fila = 5
        self.columna = 5
    
    def recibir_daño(self, daño):
        self.vida -= daño
        if self.vida < 0:
            self.vida = 0
    
    def destruida(self):
        return self.vida <= 0
    