#Autor: Virginia Riego del Castillo
def mostrar_operaciones():
    print("Las operaciones de la CALCULADORA son:")
    print("1-Sumar")
    print("2-Restar")
    print("3-Multiplicar")
    print("4-Dividir")
    try:
        operacion = int(input("Introduzca el número de la operación: "))
    except ValueError:
        print("El dato introducido no es un número entero.")
        #Volvemos a mostrar y solicitar el dato
        return mostrar_operaciones()
    #Continuación normal del programa si no ha habido errores
    else:
        if (operacion > 4) or (operacion <= 0):
            print("La opción elegida no es posible, vuelva a intentarlo.")
            return mostrar_operaciones()
        else:
            return operacion

def leer_numeros():
    try:
        #Leer el primer número y guardarlo en a
        a = int(input("Introduzca el primer número: "))
        #Leer el segundo número y guardarlo en b
        b = int(input("Introduzca el segundo número: "))
    #Decimos que tipo de exccepción puede ser lanzado
    except ValueError:
        print("El dato introducido no es un número entero.")
        return leer_numeros()
    #Continuación normal del programa si no ha habido errores
    else:
        return [a,b]

def operar(operacion, operandos):
    if operacion == 1:
        solucion = operandos[0]+operandos[1]
    elif operacion == 2:
        solucion = operandos[0]-operandos[1]
    elif operacion == 3:
        solucion = operandos[0]*operandos[1]
    elif operacion == 4:
        solucion = operandos[0]/operandos[1]
    return solucion

def salir():
    respuesta = input("¿Desea continuar? (si/no)")
    #Si las respuestas son las posibles la devolvemos
    if (respuesta == "si") or (respuesta == "no"):
        return respuesta
    #Sino repetimos la pregunta
    else:
        return salir()

#INICIO DE LA CALCULADORA
continuar = "si"
while continuar == "si":
    #Mostrar las operaciones
    operacion = mostrar_operaciones()
    #Leer los operandos para la operacion
    operandos = leer_numeros()
    #Calcular la operacion y mostrarla la solucion
    solucion = operar(operacion,operandos)
    print("La solución es: "+ str(solucion))
    #Preguntar si continuar
    continuar = salir()
