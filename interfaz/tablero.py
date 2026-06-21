import tkinter as tk

from modelos.base import Base
from modelos.muro import Muro

from modelos.unidad import (
    Unidad,
    Soldado,
    Caballero,
    Explorador
)

from modelos.torre import (
    Torre,
    TorreArquero,
    TorreCatapulta,
    TorreMago
)



class Tablero:

    def __init__(self, mapa,jugador,faccion):

        self.mapa = mapa

        # Objeto que se colocará al hacer clic
        self.objeto_seleccionado = "arquero"
        self.modo = "defensa"
        
        self.ventana = tk.Tk()
        self.ventana.title("Defensa y Asalto de Base")
        self.label_faccion = tk.Label(
            self.ventana,
            text=f"Facción: {self.faccion}",
            font=("Arial", 12, "bold")
        )

        self.label_faccion.grid(
            row=12,
            column=0,
            columnspan=5
        )
        
        self.botones = []

        self.jugador = jugador
        self.faccion = faccion
        
        self.label_dinero = tk.Label(
            self.ventana,
            text=f"Dinero: {self.jugador.dinero}",
            font=("Arial", 12, "bold")
        )

        self.label_dinero.grid(row=11, column=0, columnspan=5)
        
        
        
        
        
        tk.Button(
            self.ventana,
            text="Arquero",
            command=lambda: self.seleccionar_objeto("arquero")
        ).grid(row=0, column=11)

        tk.Button(
            self.ventana,
            text="Catapulta",
            command=lambda: self.seleccionar_objeto("catapulta")
        ).grid(row=1, column=11)

        tk.Button(
            self.ventana,
            text="Mago",
            command=lambda: self.seleccionar_objeto("mago")
        ).grid(row=2, column=11)

        tk.Button(
            self.ventana,
            text="Muro",
            command=lambda: self.seleccionar_objeto("muro")
        ).grid(row=3, column=11)
        
        tk.Button(
            self.ventana,
            text="Soldado",
            command=lambda: self.seleccionar_objeto("soldado")
        ).grid(row=6, column=11)

        tk.Button(
            self.ventana,
            text="Caballero",
            command=lambda: self.seleccionar_objeto("caballero")
        ).grid(row=7, column=11)

        tk.Button(
        self.ventana,
        text="Explorador",
        command=lambda: self.seleccionar_objeto("explorador")
        ).grid(row=8, column=11)
        
        tk.Button(
            self.ventana,
            text="Iniciar Combate",
            command=self.iniciar_combate
        ).grid(row=5, column=11)
        
        
        for fila in range(10):

            fila_botones = []

            for columna in range(10):

                boton = tk.Button(
                    self.ventana,
                    width=4,
                    height=2,
                    command=lambda f=fila, c=columna:
                    self.click_casilla(f, c)
                )

                boton.grid(
                    row=fila,
                    column=columna
                )

                fila_botones.append(boton)

            self.botones.append(fila_botones)

        self.dibujar_mapa()

        self.ventana.mainloop()

    def actualizar_dinero(self):

            self.label_dinero.config(
                text=f"Dinero: {self.jugador.dinero}"
            )    
    def seleccionar_objeto(self, objeto):
            self.objeto_seleccionado = objeto
        
    def iniciar_combate(self):

        self.mapa.ejecutar_turno()

        self.dibujar_mapa()
    
          
    def dibujar_mapa(self):

        for fila in range(10):

            for columna in range(10):

                objeto = self.mapa.matriz[fila][columna]

                texto = ""

                if self.faccion == "Medieval":

                    if isinstance(objeto, Base):
                        texto = "🏰"

                    elif isinstance(objeto, Muro):
                        texto = "🧱"

                    elif isinstance(objeto, Torre):
                        texto = "🏹"

                    elif isinstance(objeto, Unidad):
                        texto = "⚔️"

                elif self.faccion == "Futurista":

                    if isinstance(objeto, Base):
                        texto = "🤖"

                    elif isinstance(objeto, Muro):
                        texto = "⚙️"

                    elif isinstance(objeto, Torre):
                        texto = "🔫"

                    elif isinstance(objeto, Unidad):
                        texto = "🚀"

                elif self.faccion == "Naturaleza":

                    if isinstance(objeto, Base):
                        texto = "🌳"

                    elif isinstance(objeto, Muro):
                        texto = "🍃"

                    elif isinstance(objeto, Torre):
                        texto = "🌿"

                    elif isinstance(objeto, Unidad):
                        texto = "🐺"

                self.botones[fila][columna].config(
                    text=texto
                )

    def click_casilla(self, fila, columna):

        if self.mapa.obtener_objeto(fila, columna) is None:

            if self.objeto_seleccionado == "arquero":
                objeto = TorreArquero()

            elif self.objeto_seleccionado == "catapulta":
                objeto = TorreCatapulta()

            elif self.objeto_seleccionado == "mago":
                objeto = TorreMago()

            elif self.objeto_seleccionado == "muro":
                objeto = Muro()

            elif self.objeto_seleccionado == "soldado":
                objeto = Soldado()

            elif self.objeto_seleccionado == "caballero":
                objeto = Caballero()

            elif self.objeto_seleccionado == "explorador":
                objeto = Explorador()
            
            else:
                return

            if self.jugador.comprar(objeto):

                self.mapa.colocar_objeto(
                    fila,
                    columna,
                    objeto
                )

                self.actualizar_dinero()

                self.dibujar_mapa()

            else:
                print("Dinero insuficiente")