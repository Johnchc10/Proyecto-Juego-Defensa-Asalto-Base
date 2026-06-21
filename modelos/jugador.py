import json #Importamos la biblioteca json para trabajar con archivos JSON
class Jugador:#Clase para representar a un jugador en el juego
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
        self.victorias_defensor = 0
        self.victorias_atacante = 0
    
    def guardar_jugador(self):
        try:
            # Cargar los jugadores existentes desde el archivo JSON
            with open('datos/jugadores.json', 'r') as archivo:
                jugadores = json.load(archivo)
        except: #Si el archivo no existe o está vacío, inicializamos una lista vacía
            jugadores = {}
        
        jugadores[self.usuario] = {
            'contraseña': self.contraseña,
            'victorias_defensor': self.victorias_defensor,
            'victorias_atacante': self.victorias_atacante
        }
        
        # Guardar los jugadores actualizados en el archivo JSON
        with open('datos/jugadores.json', 'w') as archivo:
            json.dump(jugadores, archivo, indent=4) # Guardamos el diccionario de jugadores en el archivo JSON con una indentación de 4 espacios para mejorar la legibilidad
        
    def registrar(self):
        # Método para registrar un nuevo jugador
        try:
            with open('datos/jugadores.json', 'r') as archivo:
                jugadores = json.load(archivo)
        except:
            jugadores = {}
        
        if self.usuario in jugadores:
            return False
        
        self.guardar_jugador()
        return True
    
    @staticmethod # Método estático para verificar las credenciales de un jugador
    def iniciar_sesion(usuario, contraseña):
        try:
            with open('datos/jugadores.json', 'r') as archivo:
                jugadores = json.load(archivo)
        except:
            return None
        
        if usuario in jugadores:
            if jugadores[usuario]['contraseña'] == contraseña:
                jugador = Jugador(usuario, contraseña)
                jugador.victorias_defensor = jugadores[usuario]['victorias_defensor']
                jugador.victorias_atacante = jugadores[usuario]['victorias_atacante']
                return jugador
        
        return None