#Creacción del diccionario (pueden cambiar el orden de los elementos)
diccionario = {"Maria":5, "Juan":8, "Marta":3, "Lucas":4}
print("El diccionario creado: "+str(diccionario))
#Acceder al dato de Marta
dato = diccionario["Marta"]
print("El dato de Marta es: "+str(dato))
#Añadir nuevos datos al diccionario
diccionario["Luisa"] = 10
print("El diccionario cambiado: "+str(diccionario))
#Se puede poner cualquier tipo de dato
diccionario["Juan"] = "siete"
print("El diccionario cambiado: "+str(diccionario))
#Para cambiar los valores de los datos
diccionario.update({"Maria":5, "Marta":6, "Lucas": 7})
print("El diccionario actualizado: "+str(diccionario))
#Otra forma de crear diccionarios es con listas
diccionario2 = dict([["Maria",5],["Juan",8],["Marta",3]])
print("El diccionario nuevo: "+str(diccionario2))
#Para borrar un elemento del diccionario
del diccionario2["Marta"]
print("El diccionario nuevo borrando: "+str(diccionario2))
#Recorriendo los Diccionarios
print("Recorriendo el diccionario")
for valor in diccionario:
    print(str(valor)+"--> "+str(diccionario[valor]))
print("Recorriendo el diccionario de otra manera")
for valor in diccionario.keys():
    print(str(valor)+"--> "+str(diccionario[valor]))
print("Recorriendo el diccionario para valores")
for valor in diccionario.values():
    print(str(valor))
print("Recorriendo el diccionario de otra manera")
for tupla in diccionario.items():
    print(tupla)
