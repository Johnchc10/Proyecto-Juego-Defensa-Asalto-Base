import tkinter as tk
from interfaz.ranking import Ranking

from modelos.jugador import Jugador
from modelos.gestor_partida import GestorPartida

from interfaz.roles import Roles
from interfaz.facciones import Facciones

from modelos.mapa import Mapa
from interfaz.tablero import Tablero

from interfaz.login_partida import LoginPartida

class Menu:
    def __init__(self):
        # Crear la ventana principal del menú
        self.ventana = tk.Tk()
        self.ventana.title("Menú Principal")
        self.ventana.geometry("400x300")
    
        titulo = tk.Label(
            self.ventana, 
            text="Defensa y Asalto a la Base",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=20)
        
        # Botones del menú
        tk.Button(
            self.ventana, 
            text="Iniciar Juego", 
            width=20,
            command=self.iniciar_partida
        ).pack(pady=10)
        
        tk.Button(
            self.ventana, 
            text="Ranking", 
            width=20,
            command=self.ver_ranking
        ).pack(pady=10)
        
        tk.Button(
            self.ventana, 
            text="Salir", 
            width=20,
            command=self.ventana.destroy
        ).pack(pady=10)
        
        self.ventana.mainloop()
    
    def iniciar_partida(self):
        self.ventana.destroy()
        gestor = GestorPartida()

        login1 = LoginPartida()

        jugador1 = login1.obtener_jugador()

        if jugador1 is None:
            return

        login2 = LoginPartida()

        jugador2 = login2.obtener_jugador()

        if jugador2 is None:
            return
        
        if jugador1.usuario == jugador2.usuario:

            from tkinter import messagebox

            messagebox.showerror(
                "Error",
                "Los jugadores deben ser diferentes"
            )

            return
        
        
        gestor.asignar_jugadores(
            jugador1,
            jugador2
        )

        roles = Roles(
            jugador1,
            jugador2
        )

        gestor.asignar_roles(
            roles.obtener_defensor(),
            roles.obtener_atacante()
        )

        facciones = Facciones()

        gestor.asignar_facciones(
            facciones.obtener_faccion_defensor(),
            facciones.obtener_faccion_atacante()
        )

        print(
            "Defensor:",
            gestor.defensor.usuario
        )

        print(
            "Atacante:",
            gestor.atacante.usuario
        )

        print(
            "Facción defensor:",
            gestor.faccion_defensor
        )

        print(
            "Facción atacante:",
            gestor.faccion_atacante
        )
        mapa = Mapa()

        Tablero(
            mapa,
            gestor.defensor,
            gestor.atacante,
            gestor.faccion_defensor,
            gestor.faccion_atacante
        )
    def ver_ranking(self):
        Ranking()
        
        