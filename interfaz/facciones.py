import tkinter as tk
from tkinter import messagebox

class Facciones:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Seleccionar Facción")
        self.ventana.geometry("400x300")
        
        self.label = tk.Label(
            self.ventana,
            text="Selecciona la facción del Defensor:"
        )

        self.label.pack(pady=20)
        
        self.faccion = tk.StringVar()#Variable para almacenar la facción seleccionada
        
        self.faccion_defensor = None
        self.faccion_atacante = None

        self.etapa = 1
        
        #Crear opciones de facciones
        tk.Radiobutton(self.ventana, text="Medieval", variable=self.faccion, value="Medieval").pack()
        tk.Radiobutton(self.ventana, text="Futurista", variable=self.faccion, value="Futurista").pack()
        tk.Radiobutton(self.ventana, text="Naturaleza", variable=self.faccion, value="Naturaleza").pack()
        
        tk.Button(self.ventana, text="Continuar", command=self.continuar).pack(pady=20)
        
        self.ventana.mainloop()
        
    def continuar(self):

        if self.faccion.get() == "":
            messagebox.showerror(
                "Error",
                "Selecciona una facción"
            )
            return

        if self.etapa == 1:

            self.faccion_defensor = self.faccion.get()

            self.etapa = 2

            self.faccion.set("")

            self.label.config(
                text="Selecciona la facción del Atacante:"
            )

        else:

            if self.faccion.get() == self.faccion_defensor:

                messagebox.showerror(
                    "Error",
                    "No pueden usar la misma facción"
                )

                return

            self.faccion_atacante = self.faccion.get()

            print(
                "Defensor:",
                self.faccion_defensor
            )

            print(
                "Atacante:",
                self.faccion_atacante
            )

            self.ventana.destroy()
    def obtener_faccion_defensor(self):
        return self.faccion_defensor

    def obtener_faccion_atacante(self):
        return self.faccion_atacante       