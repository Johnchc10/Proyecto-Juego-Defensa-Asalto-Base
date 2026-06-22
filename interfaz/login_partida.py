import tkinter as tk
from tkinter import messagebox

from modelos.jugador import Jugador


class LoginPartida:

    def __init__(self):

        self.jugador = None

        self.ventana = tk.Tk()
        self.ventana.title("Login Jugador")
        self.ventana.geometry("300x200")

        tk.Label(
            self.ventana,
            text="Usuario"
        ).pack()

        self.usuario_entry = tk.Entry(
            self.ventana
        )
        self.usuario_entry.pack()

        tk.Label(
            self.ventana,
            text="Contraseña"
        ).pack()

        self.contra_entry = tk.Entry(
            self.ventana,
            show="*"
        )
        self.contra_entry.pack()

        tk.Button(
            self.ventana,
            text="Ingresar",
            command=self.login
        ).pack(pady=10)

        self.ventana.mainloop()

    def login(self):

        usuario = self.usuario_entry.get()
        contra = self.contra_entry.get()

        jugador = Jugador.iniciar_sesion(
            usuario,
            contra
        )

        if jugador:

            self.jugador = jugador

            self.ventana.destroy()

        else:

            messagebox.showerror(
                "Error",
                "Credenciales incorrectas"
            )

    def obtener_jugador(self):

        return self.jugador