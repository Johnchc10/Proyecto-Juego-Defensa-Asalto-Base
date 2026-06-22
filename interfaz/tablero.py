import tkinter as tk
from modelos.partida import Partida
from modelos.base import Base
from modelos.muro import Muro
from tkinter import messagebox



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

    def __init__(self, mapa,defensor,atacante,faccion):

        self.mapa = mapa

        # Objeto que se colocará al hacer clic
        self.objeto_seleccionado = "arquero"
        self.modo = "defensa"
        
        self.ventana = tk.Tk()
        self.ventana.title("Defensa y Asalto de Base")
        self.botones = []
        self.ventana.geometry("900x700")
        
        self.label_modo = tk.Label(
            self.ventana,
            text="Turno del Defensor",
            font=("Arial", 12, "bold")
        )

        self.label_modo.grid(
            row=15,
            column=0,
            columnspan=5
        )
        
       
        
        self.defensor = defensor
        self.atacante = atacante
        self.faccion = faccion
        self.partida = Partida()
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
        
        
        
        self.label_dinero = tk.Label(
            self.ventana,
            text=f"Dinero: {self.defensor.dinero}",
            font=("Arial", 12, "bold")
        )

        self.label_dinero.grid(row=11, column=0, columnspan=5)
        
        self.label_ronda = tk.Label(
            self.ventana,
            text="Ronda 1",
            font=("Arial", 12, "bold")
        )

        self.label_ronda.grid(
            row=13,
            column=0,
            columnspan=5
        )
        
        self.label_marcador = tk.Label(
            self.ventana,
            text="Defensor: 0 | Atacante: 0",
            font=("Arial", 12, "bold")
        )

        self.label_marcador.grid(
            row=14,
            column=0,
            columnspan=5
        )
        
        
        
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
            text="Pasar al Atacante",
            command=self.cambiar_a_ataque
        ).grid(row=4, column=11)

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
                    width=6,
                    height=3,
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

        if self.modo == "defensa":

            dinero = self.defensor.dinero

        else:

            dinero = self.atacante.dinero

        self.label_dinero.config(
            text=f"Dinero: {dinero}"
        )
    
    def actualizar_marcador(self):

        self.label_marcador.config(
            text=
            f"Defensor: {self.partida.victorias_defensor} | "
            f"Atacante: {self.partida.victorias_atacante}"
        )
    
    def seleccionar_objeto(self, objeto):
            self.objeto_seleccionado = objeto
    
    def cambiar_a_ataque(self):

        self.modo = "ataque"

        self.label_modo.config(
            text="Turno del Atacante"
        )

        messagebox.showinfo(
            "Cambio de turno",
            "Ahora el atacante puede colocar unidades"
        )
      
    def iniciar_combate(self):

        if self.modo == "defensa":

            messagebox.showwarning(
                "Advertencia",
                "Primero debes pasar al atacante"
            )

            return

        self.mapa.ejecutar_turno()

        resultado = self.partida.verificar_ganador_ronda(
            self.mapa,
            self.defensor,
            self.atacante
        )

        if resultado:

            messagebox.showinfo(
                "Fin de ronda",
                f"Gana el {resultado}"
            )

            self.actualizar_marcador()

            if self.partida.partida_terminada():

                if self.partida.victorias_defensor >= 3:

                    messagebox.showinfo(
                        "Fin de partida",
                        "¡El defensor gana la partida!"
                    )

                else:

                    messagebox.showinfo(
                        "Fin de partida",
                        "¡El atacante gana la partida!"
                    )

                self.ventana.destroy()

                return

            self.partida.ronda += 1

            self.label_ronda.config(
                text=f"Ronda {self.partida.ronda}"
            )

            self.mapa.reiniciar()

            self.defensor.agregar_dinero(100)
            self.atacante.agregar_dinero(100)

            self.modo = "defensa"

            self.label_modo.config(
                text="Turno del Defensor"
            )

            self.actualizar_dinero()

            self.dibujar_mapa()

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
            if self.modo == "defensa":

                if self.objeto_seleccionado in [
                    "soldado",
                    "caballero",
                    "explorador"
                ]:

                    messagebox.showerror(
                        "Error",
                        "Solo el atacante puede colocar unidades"
                    )

                    return

            if self.modo == "ataque":

                if self.objeto_seleccionado in [
                    "arquero",
                    "catapulta",
                    "mago",
                    "muro"
                ]:

                    messagebox.showerror(
                        "Error",
                        "Solo el defensor puede colocar estructuras"
                    )

                    return
            
            
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

            if self.modo == "defensa":

                comprado = self.defensor.comprar(objeto)

            else:

                comprado = self.atacante.comprar(objeto)

            if comprado:

                self.mapa.colocar_objeto(
                    fila,
                    columna,
                    objeto
                )

                self.actualizar_dinero()

                self.dibujar_mapa()

            else:
                messagebox.showerror(
                    "Error",
                    "Dinero insuficiente"
                )