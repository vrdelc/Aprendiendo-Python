#Del archivo jugador.py importar la clase Jugador
from jugador import Jugador
from tablero import Tablero
from jugador import Premium
#Jugador por defecto
jugador = Jugador()
print("El nombre del jugador por defecto es {} y tiene {} vidas".format(jugador.nombre, jugador.vidas))

#Creamos los objetos
jugador1 = Jugador("Luis")
jugador2 = Jugador("Maria")

#Cambiamos los atriutos
jugador1.vidas = 10
print("El nombre del jugador 1 es {} y tiene {} vidas".format(jugador1.nombre, jugador1.vidas))
jugador2.vidas = 8
print("El nombre del jugador 2 es {} y tiene {} vidas".format(jugador2.nombre, jugador2.vidas))

#Utilización de métodos
jugador1.quitarVida()
print("El jugador 1 actualizado es {} y tiene {} vidas".format(jugador1.obtenerNombre(), jugador1.vidas))

#Objetos a partir de diccionarios
tablero1 = Tablero(dificultad=1, ancho=20, alto=10)
print("El tablero 1 tiene dificultad {} y dimensiones {}x{}".format(tablero1.dificultad,tablero1.ancho,tablero1.alto))
#Objeto con creación de datos por defecto
tablero2 = Tablero(dificultad=2)
#Impresión de la información del objeto
print(tablero2)

#Objetos con herencia
jugadorP = Premium()
print("El nombre del jugador premium es {} y tiene {} vidas".format(jugadorP.nombre, jugadorP.vidas))
#Sobreescribir métodos
print("El nombre del jugador premium es {} y tiene {} vidas".format(jugadorP.obtenerNombre(), jugadorP.vidas))