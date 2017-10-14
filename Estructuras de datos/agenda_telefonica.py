def mostrar_operaciones():
    print()
    print("----------------------------------------------")
    print("Estas son las operaciones que puedes realizar:")
    print("1. Agregar contacto")
    print("2. Borrar contacto")
    print("3. Actualizar un contacto")
    print("4. Ver un contacto")
    print("5. Ver todos los contacto")
    print("6. Salir")
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
        if (operacion > 6) or (operacion <= 0):
            print("La opción elegida no es posible, vuelva a intentarlo.")
            return mostrar_operaciones()
        else:
            return operacion

def agregar_contacto():
    print("**AGREGANDO UN NUEVO CONTACTO**")
    nombre = input("Introduzca el nombre: ")
    telefono = input("Introduzca el teléfono: ")
    agenda[nombre]=telefono

def borrar_contacto():
    print("**BORRAR UN CONTACTO**")
    nombre = input("Introduzca el nombre: ")
    try:
        telefono = agenda[nombre]
    except KeyError:
        print("El contacto: " + nombre + " no está guardado.")
    else:
        print("El contacto: " + nombre + " tiene el telefono: "+ telefono)
        del agenda[nombre]

def actualizar_contacto():
    print("**ACTUALIZAR UN CONTACTO**")
    nombre = input("Introduzca el nombre: ")
    try:
        telefono = agenda[nombre]
    except KeyError:
        print("El contacto: " + nombre + " no está guardado.")
    else:
        print("El contacto: " + nombre + " tiene el telefono: "+ telefono)
        nombre_nuevo = input("Introduzca el nombre nuevo: ")
        telefono_nuevo = input("Introduzca el telefono nuevo: ")
        del agenda[nombre]
        agenda[nombre_nuevo] = telefono_nuevo

def ver_contacto():
    print("**VER INFORMACIÓN DE UN CONTACTO**")
    nombre = input("Introduzca el nombre: ")
    try:
        telefono = agenda[nombre]
    except KeyError:
        print("El contacto: " + nombre + " no está guardado.")
    else:
        print("El contacto: " + nombre + " tiene el telefono: "+ telefono)
        salir = input("Presione cualquier tecla para continuar: ")

def mostrar_agenda():
    print("**AGENDA**")
    contador = 1
    for tupla in agenda.items():
        print(str(contador) +": "+ str(tupla))
        contador += 1
    salir = input("Presione cualquier tecla para continuar: ")


#Creamos una lista vacia
agenda = dict()
continuar = "true"

while continuar == "true":
    operacion = mostrar_operaciones()
    if operacion == 1:
        agregar_contacto()
    elif operacion == 2:
        borrar_contacto()
    elif operacion == 3:
        actualizar_contacto()
    elif operacion == 4:
        ver_contacto()
    elif operacion == 5:
        mostrar_agenda()
    else:
        continuar = "false"
        print("Fin del programa")
