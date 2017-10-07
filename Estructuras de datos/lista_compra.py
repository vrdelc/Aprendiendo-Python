def mostrar_operaciones():
    print("----------------------------------------------")
    print("Estas son las operaciones que puedes realizar:")
    print("1. Agregar artículo")
    print("2. Borrar artículo")
    print("3. Mostrar lista")
    print("4. Salir")
    #Lectura de la operación
    try:
        operacion = int(input("Introduzca el número de la operación: "))
        print()
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

def agregar_articulo():
    articulo = input("Introduzca el artículo que desea añadir: ")
    lista.append(articulo)

def borrar_articulo():
    if len(lista) > 0:
        mostrar_lista()
        #Lectura de la operación
        try:
            operacion = int(input("Introduzca el número del artículo que desea borrar: "))
            print()
        except ValueError:
            print("El dato introducido no es un número entero.")
            #Volvemos a mostrar y solicitar el dato
            return borrar_articulo()
        #Continuación normal del programa si no ha habido errores
        else:
            if (operacion > len(lista)) or (operacion <= 0):
                print("La opción elegida no es posible, vuelva a intentarlo.")
                return borrar_articulo()
            else:
                del lista[operacion-1]
    else:
        print("La lista está vacia y no se pueden borrar artículos")

def mostrar_lista():
    print("La lista es la siguiente: ")
    contador = 1
    for articulo in lista:
        print(str(contador)+"- " + articulo)
        contador += 1

#Creamos una lista vacia
lista = list()
continuar = "true"

while continuar == "true":
    operacion = mostrar_operaciones()
    if operacion == 1:
        agregar_articulo()
    elif operacion == 2:
        borrar_articulo()
    elif operacion == 3:
        mostrar_lista()
    else:
        continuar = "false"
        print("Fin del programa")
