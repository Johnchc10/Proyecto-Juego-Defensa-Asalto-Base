import tkinter as tk
import json


class Ranking:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Ranking")
        self.ventana.geometry("500x400")

        self.mostrar_ranking()

        self.ventana.mainloop()
    
    def mostrar_ranking(self):

        try:

            with open(
                "datos/jugadores.json",
                "r",
                encoding="utf-8"
            ) as archivo:

                jugadores = json.load(archivo)

        except:

            jugadores = {}

        tk.Label(
            self.ventana,
            text="TOP DEFENSORES",
            font=("Arial", 14, "bold")
        ).pack()

        lista_defensores = []

        for usuario, datos in jugadores.items():

            lista_defensores.append(
                (
                    usuario,
                    datos["victorias_defensor"]
                )
            )

        lista_defensores.sort(
            key=lambda x: x[1],
            reverse=True
        )

        for usuario, victorias in lista_defensores[:5]:

            tk.Label(
                self.ventana,
                text=f"{usuario}: {victorias}"
            ).pack()
        
        tk.Label(
            self.ventana,
            text="",
        ).pack()

        tk.Label(
            self.ventana,
            text="TOP ATACANTES",
            font=("Arial", 14, "bold")
        ).pack()

        lista_atacantes = []

        for usuario, datos in jugadores.items():

            lista_atacantes.append(
                (
                    usuario,
                    datos["victorias_atacante"]
                )
            )

        lista_atacantes.sort(
            key=lambda x: x[1],
            reverse=True
        )

        for usuario, victorias in lista_atacantes[:5]:

            tk.Label(
                self.ventana,
                text=f"{usuario}: {victorias}"
            ).pack()  