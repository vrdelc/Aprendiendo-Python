#Importar una libreria de números aleatorios
import random

def leer_numero():
    es_numero = False
    while es_numero==False:
        try:
            usuario = int(input("Adivina el número: "))
            es_numero=True
        except ValueError:
            print("No ha introducido un número. Vuelva a intentarlo")
    return usuario

#Inicializamos las vidas
vidas = 5
print("¡Bienvenido a adivina el número!")
continuar = True
while continuar:
    print("***************Te quedan {} vidas***************".format(vidas))
    print("Estoy pensando un número entre el 1 y el 10")
    #Generar un número aletorio entre 1 y 10
    numero = random.randint(1,10)
    #Leer el dato del usuario
    usuario = leer_numero()
    #Comprobar si ha acertado
    if numero==usuario:
        print("¡Has acertado!")
        vidas = vidas + 1
    else:
        print("Te has confundido el número era: {}".format(numero))
        vidas = vidas - 1
        if vidas == 0:
            continuar = False
            print("Lo sentimos, se te han acabado las vidas.")
            break
    #División del texto para mejor visibilidad
    input()
    print()
    print("------------------------------------------------")
    print()