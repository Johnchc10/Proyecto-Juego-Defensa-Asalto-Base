class Torre: #Aquí se define la clase Torre, que representa una torre en el juego.
    def __init__(self, nombre, vida, daño, alcance, costo):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
        self.alcance = alcance
        self.costo = costo
    
    def __str__(self):
        return f"{self.nombre} | Vida: {self.vida} "
    
    def recibir_daño(self, daño):
        self.vida -= daño
        if self.vida < 0:
            self.vida = 0
    
    def destruida(self):
        return self.vida <= 0  
    
    def atacar(self, objetivo):
        objetivo.recibir_daño(self.daño)
    
class TorreArquero(Torre): #Aquí se define la clase TorreArquero, que hereda de la clase Torre y representa una torre de arqueros.
    def __init__(self):
        super().__init__("Torre de Arqueros", 100, 20, 3, 50)     
        
class TorreCatapulta(Torre): #Aquí se define la clase TorreCatapulta, que hereda de la clase Torre y representa una torre de catapultas.
    def __init__(self):
        super().__init__("Torre de Catapultas", 200, 40, 4,100)

class TorreMago(Torre): #Aquí se define la clase TorreMago, que hereda de la clase Torre y representa una torre de magos.
    def __init__(self):
        super().__init__("Torre de Magos", 80,15,4,80)
        