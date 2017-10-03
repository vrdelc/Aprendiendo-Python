#Ponemos el código que puede lanzar una excepción
try:
    #Leer el primer número y guardarlo en a
    a = int(input("Introduzca un número: "))
    #Leer el segundo número y guardarlo en b
    b = int(input("Introduzca otro número: "))
#Decimos que tipo de exccepción puede ser lanzado
except ValueError:
    print("EL dato introducido no es un número entero")
#Continuación normal del programa si no ha habido errores
else:
    suma = a + b
    print("La suma es: "+ str(suma))
