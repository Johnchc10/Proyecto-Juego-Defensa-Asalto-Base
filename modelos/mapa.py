from modelos.base import Base
from modelos.muro import Muro
from modelos.torre import Torre
from modelos.unidad import Unidad


class Mapa(Base):
    def __init__(self):
        self.filas = 10
        self.columnas = 10
        
        self.matriz = []

        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                fila.append(None)
            self.matriz.append(fila)
        
        self.base = Base()
        
        self.matriz[5][5] = self.base
        
    def mostrar(self):
        for fila in self.matriz:
            for casilla in fila:
            

                if casilla is None:
                    print("[ ]", end=" ")

                elif isinstance(casilla, Base):
                    print("[B]", end=" ")

                elif isinstance(casilla, Muro):
                    print("[M]", end=" ")

                elif isinstance(casilla, Torre):
                    print("[T]", end=" ")

                elif isinstance(casilla, Unidad):
                    print("[U]", end=" ")

            print()
    
    def colocar_objeto(self, fila, columna, objeto):

        if self.matriz[fila][columna] is None:

            self.matriz[fila][columna] = objeto

            if hasattr(objeto, "fila"):
                objeto.fila = fila
                objeto.columna = columna

            return True

        return False
    
    def obtener_objeto(self,fila,columna):
        return self.matriz[fila][columna]
    
    def eliminar_objeto(self, fila, columna):
        self.matriz[fila][columna] = None       
    
    def verificar_destruido(self, fila, columna):

        objeto = self.obtener_objeto(
            fila,
            columna
        )

        if objeto is not None:

            if hasattr(objeto, "destruido"):

                if objeto.destruido():
                    self.eliminar_objeto(
                        fila,
                        columna
                    )

        elif hasattr(objeto, "destruida"):

            if objeto.destruida():
                self.eliminar_objeto(
                    fila,
                    columna
                )
    def obtener_unidades(self):

        unidades = []

        for fila in self.matriz:

            for casilla in fila:

                if isinstance(casilla, Unidad):
                    unidades.append(casilla)

        return unidades
    
    def obtener_torres(self):

        torres = []

        for fila in self.matriz:

            for casilla in fila:

                if isinstance(casilla, Torre):
                    torres.append(casilla)

        return torres
    
    def ejecutar_turno(self):

        torres = self.obtener_torres()

        for torre in torres:

            objetivo = self.buscar_unidad_mas_cercana(torre)

            if objetivo:
                torre.atacar(objetivo)

        self.limpiar_destruidos()

        unidades = self.obtener_unidades()

        for unidad in unidades:
            unidad.mover(self)

        self.limpiar_destruidos()
    
    def buscar_unidad_mas_cercana(self, torre):

        for fila in self.matriz:

            for casilla in fila:

                if isinstance(casilla, Unidad):

                    distancia = abs(casilla.fila - torre.fila) + abs(casilla.columna - torre.columna)

                    if distancia <= torre.alcance:
                        return casilla

        return None
    
    def limpiar_destruidos(self):

        for fila in range(self.filas):

            for columna in range(self.columnas):

                objeto = self.matriz[fila][columna]

                if objeto is not None:

                    if hasattr(objeto, "destruido"):

                        if objeto.destruido():
                            self.matriz[fila][columna] = None

                    elif hasattr(objeto, "destruida"):

                        if objeto.destruida():
                            self.matriz[fila][columna] = None
    def base_destruida(self):

        return self.base.destruida()
    def quedan_unidades(self):

        for fila in self.matriz:

            for casilla in fila:

                if isinstance(casilla, Unidad):
                    return True

        return False