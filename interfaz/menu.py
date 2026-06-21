import tkinter as tk

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
        print("Iniciar partida")
    
    def ver_ranking(self):
        print("Ver ranking")
        
        