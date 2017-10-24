class Jugador:

    #Atributos de la clase
    vidas = 5

    #Constructor
    def __init__(self, nombre="Jugador1"):
        self.nombre = nombre

    #Métodos de la clase
    def quitarVida(self):
        self.vidas = self.vidas - 1

    def obtenerNombre(self):
        return self.nombre

class Premium(Jugador):
    #Cambiar los atributos
    vidas = 10
    #Sobreescribir el método
    def obtenerNombre(self):
        return "{}_premium".format(self.nombre)