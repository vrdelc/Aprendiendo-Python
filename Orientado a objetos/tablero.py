class Tablero:
    
    #Constructor
    def __init__(self, **kwargs):
        self.dificultad = kwargs.get("dificultad")
        #Poner valores por defecto si no están definidos
        self.ancho= kwargs.get("ancho",20)
        self.alto= kwargs.get("alto",20)

    #Información para la impresión del objeto
    def __str__(self):
        return "El tablero 2 tiene dificultad {} y dimensiones {}x{}".format(self.dificultad,self.ancho,self.alto)