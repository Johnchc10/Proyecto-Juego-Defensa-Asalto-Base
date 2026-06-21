import tkinter as tk

from modelos.base import Base
from modelos.muro import Muro
from modelos.torre import Torre
from modelos.unidad import Unidad


class Tablero:

    def __init__(self, mapa):

        self.mapa = mapa

        self.ventana = tk.Tk()
        self.ventana.title("Defensa y Asalto de Base")

        self.botones = []

        for fila in range(10):

            fila_botones = []

            for columna in range(10):

                boton = tk.Button(
                    self.ventana,
                    width=4,
                    height=2,
                    text=""
                )

                boton.grid(
                    row=fila,
                    column=columna
                )

                fila_botones.append(boton)

            self.botones.append(fila_botones)

        self.dibujar_mapa()

        self.ventana.mainloop()

    def dibujar_mapa(self):

        for fila in range(10):

            for columna in range(10):

                objeto = self.mapa.matriz[fila][columna]

                texto = ""

                if isinstance(objeto, Base):
                    texto = "B"

                elif isinstance(objeto, Muro):
                    texto = "M"

                elif isinstance(objeto, Torre):
                    texto = "T"

                elif isinstance(objeto, Unidad):
                    texto = "U"

                self.botones[fila][columna].config(
                    text=texto
                )