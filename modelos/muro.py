class Muro:
    def __init__(self):
        self.vida = 150
        self.costo = 100
        self.fila = None
        self.columna = None
        
        
        
    def recibir_daño(self, daño):
        self.vida -= daño
        if self.vida < 0:
            self.vida = 0
    
    def destruido(self):
        return self.vida <= 0
    
    def __str__(self):
        return f"Muro | Vida: {self.vida} "