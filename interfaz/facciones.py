import tkinter as tk
from tkinter import messagebox

class SeleccionFaccion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Seleccionar Facción")
        self.ventana.geometry("400x300")
        
        tk.Label(self.ventana, text="Selecciona tu facción:").pack(pady=20)
        
        self.faccion = tk.StringVar()#Variable para almacenar la facción seleccionada
        
        #Crear opciones de facciones
        tk.Radiobutton(self.ventana, text="Medieval", variable=self.faccion, value="Medieval").pack()
        tk.Radiobutton(self.ventana, text="Futurista", variable=self.faccion, value="Futurista").pack()
        tk.Radiobutton(self.ventana, text="Naturaleza", variable=self.faccion, value="Naturaleza").pack()
        
        tk.Button(self.ventana, text="Continuar", command=self.continuar).pack(pady=20)
        
        self.ventana.mainloop()
        
    def continuar(self):
        if self.faccion.get() == "":
            messagebox.showerror("Error", "Por favor, selecciona una facción")
        else:
            messagebox.showinfo("Facción seleccionada", f"Has seleccionado la facción: {self.faccion.get()}")
            
            