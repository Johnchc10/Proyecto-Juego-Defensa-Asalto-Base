class Unidad:
    
    def __init__(self, nombre, vida, daño, velocidad, costo):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
        self.velocidad = velocidad
        self.costo = costo
        self.fila = None
        self.columna = None
    
    def recibir_daño(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0
    
    def destruida(self):
        return self.vida <= 0
    
    def __str__(self):
        return f"{self.nombre} | Vida: {self.vida} "

    def atacar(self, objetivo):
        objetivo.recibir_daño(self.daño)
    
    def mover(self, mapa):

        nueva_columna = self.columna + self.velocidad

        if nueva_columna > 9:
            nueva_columna = 9

        objeto = mapa.obtener_objeto(
            self.fila,
            nueva_columna
        )

        if objeto is None:

            mapa.eliminar_objeto(
                self.fila,
                self.columna
            )

            self.columna = nueva_columna

            mapa.colocar_objeto(
                self.fila,
                self.columna,
                self
            )

        else:
            self.atacar(objeto)
    
class Soldado(Unidad):
    
    def __init__(self):
        super().__init__("Soldado", 100, 20, 1, 50)

class Caballero(Unidad):
    
    def __init__(self):
        super().__init__("Caballero", 250, 35, 1, 120)
        
class Explorador(Unidad):
    
    def __init__(self):
        super().__init__("Explorador", 70, 15, 2, 60)
    
