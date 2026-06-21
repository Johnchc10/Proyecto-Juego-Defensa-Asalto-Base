import tkinter as tk


class Roles:

    def __init__(self, jugador1, jugador2):

        self.jugador1 = jugador1
        self.jugador2 = jugador2

        self.defensor = None
        self.atacante = None
        
        self.roles_asignados = False

        self.ventana = tk.Tk()
        self.ventana.title("Seleccionar Roles")
        self.ventana.geometry("400x250")

        tk.Label(
            self.ventana,
            text=f"Jugador 1: {jugador1.usuario}"
        ).pack(pady=10)

        tk.Label(
            self.ventana,
            text=f"Jugador 2: {jugador2.usuario}"
        ).pack(pady=10)

        tk.Button(
            self.ventana,
            text=f"{jugador1.usuario} será Defensor",
            command=self.jugador1_defensor
        ).pack(pady=5)

        tk.Button(
            self.ventana,
            text=f"{jugador2.usuario} será Defensor",
            command=self.jugador2_defensor
        ).pack(pady=5)

        self.ventana.mainloop()
    
    def jugador1_defensor(self):

        self.defensor = self.jugador1
        self.atacante = self.jugador2
        self.roles_asignados = True
        print("Defensor:", self.defensor.usuario)
        print("Atacante:", self.atacante.usuario)
        

        self.ventana.destroy()

    def jugador2_defensor(self):

        self.defensor = self.jugador2
        self.atacante = self.jugador1
        self.roles_asignados = True
        
        print("Defensor:", self.defensor.usuario)
        print("Atacante:", self.atacante.usuario)

        self.ventana.destroy()
        
    def obtener_defensor(self):
        return self.defensor

    def obtener_atacante(self):
        return self.atacante