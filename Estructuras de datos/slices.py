numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Recordar que para obtener el elemento de un índice concreto
print("Dato en indice 3: "+str(numeros[3]))
#Sin embargo, para seleccionar del 1 al 5 utilizariamos
seleccion=numeros[1:6]
#El número de comienzo está incluido, pero el último no está incluido
print("Lista del 1 al 5: "+str(seleccion))
#Si ponemmos un índice que es mayor a la longitud de la lista, llega hasta el final sin error
try:
    prueba = numeros[11]
except IndexError as e:
    print("Se ha producido el error al seleccionar indice 11: " + str(e))
seleccion2 = numeros[6:11]
print("Lista del 6 al final: "+str(seleccion2))
#Otra opción de seleccionar hasta el final
seleccion3 = numeros[6:]
print("Lista del 6 al final(otra manera): "+str(seleccion3))
#Para seleccionar desde el inicio a un número
seleccion4 = numeros[:4]
print("Lista del inicio al 3: "+str(seleccion4))
#Para seleccionar todos
seleccion5 = numeros[:]
print("Selección de la lista: "+str(seleccion5))
#También funciona con índices negativos
seleccion6 = numeros[-5:-2]
print("Selección con números negativos: "+str(seleccion6))

#A continuación hablaremos de los slices con saltos
print("------")
#Para seleccionar cada dos de toda la lista
saltos = numeros[::2]
print("Selección pares de la lista: "+str(saltos))
#Esto también se puede hacer poniendo inicio y fin
saltos2 = numeros[1:10:2]
print("Selección impares de la lista: "+str(saltos2))
#Así como con los negativos, que nos puede permitir cambiar el orden
saltos3 = numeros[::-1]
print("Lista inversa: "+str(saltos3))
#Para borrar elementos de una lista
del numeros[7:]
print("Lista acortada: "+str(numeros))
#Borraremos los pares
del numeros[::2]
print("Lista sin pares: "+str(numeros))
#Para remplazar elementos de la lista
numeros[1:3] = [3,4,5]
print("Lista con reemplazos: "+str(numeros))
