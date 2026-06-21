import tkinter as tk

class Tablero:

    def __init__(self):

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

        self.ventana.mainloop()