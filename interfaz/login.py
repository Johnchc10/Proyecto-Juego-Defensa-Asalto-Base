import tkinter as tk
from modelos.jugador import Jugador
from tkinter import messagebox
from interfaz.menu import Menu

class Login:
    def __init__(self):
        # Crear la ventana principal del login
        self.ventana = tk.Tk()
        self.ventana.title("Login - Defensa y Asalto a la Base")
        self.ventana.geometry("400x300")
        #Usuario
        tk.Label(self.ventana, text="Usuario:").pack()
        self.usuario_entry = tk.Entry(self.ventana)
        self.usuario_entry.pack()
        
        #Contraseña
        tk.Label(self.ventana, text="Contraseña:").pack()
        self.contra_entry = tk.Entry(self.ventana, show="*")
        self.contra_entry.pack()
        
        #Botón de login
        tk.Button(self.ventana, text="Iniciar Sesión", command=self.login).pack()
        
        #Botón de registro
        tk.Button(self.ventana, text="Registrarse", command=self.registrarse).pack()
        
        self.ventana.mainloop()
        
    def login(self):#Función para manejar el proceso de inicio de sesión
        usuario = self.usuario_entry.get()
        contra = self.contra_entry.get()
        jugador = Jugador.iniciar_sesion(usuario, contra)
            
        if jugador:
            messagebox.showinfo("Login exitoso", f"Bienvenido, {jugador.usuario}!")
            # Cerrar la ventana de login y abrir el menú principal
            self.ventana.destroy()
            Menu()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def registrarse(self):#Función para manejar el proceso de registro
        #Obtener el usuario y la contraseña ingresados por el usuario
        usuario = self.usuario_entry.get()
        contra = self.contra_entry.get()
            
        jugador = Jugador(usuario, contra)
            
        if jugador.registrar():#Si el registro es exitoso, se muestra un mensaje de éxito
            messagebox.showinfo("Registro exitoso", f"Usuario registrado: {jugador.usuario}")
            
        else:
            messagebox.showerror("Error", "El usuario ya existe")
        
  