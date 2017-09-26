#Lista gurdada en una variable
lista = [1,2,3]
print(lista)
#Concatenación en listas
lista = lista + [4,5]
print(lista)
lista += [6,7]
print(lista)
lista.append(8)
print(lista)
lista.extend([9,10])
print(lista)
#Repetición de los elementos de la lista
lista_repetida = lista * 4
print (lista_repetida)
# Más datos dentro de la lista
lista_completa = lista
lista_completa.append("hola")
print (lista_completa)
lista_completa.append( [5,6,7,8] )
print (lista_completa)
#Eliminar un dato de la lista
lista_completa.remove(4)
print (lista_completa)
#Creación de listas con el método list
lista2 = list([1,2,3,4])
print(lista2)
cadena = "hola mundo"
lista_letras = list(cadena)
print(lista_letras)
#Crear una lista a partir de una cadena
lista_frase = cadena.split()
print(lista_frase)
lista_frase_o = cadena.split("o")
print(lista_frase_o)
#Generar una cadena a partir de una lista
frase = " ".join(lista_frase)
print(frase)
frase_o = "o".join(lista_frase_o)
print(frase_o)
#Obtener el indice de un elemento de la lista
indice = frase.index("a")
print(indice)
#Para acceder a un elemento de una lista
letra = frase[0]
print(letra)
#IMPORTANTE: existen los indices negativos, se leen empezando por el final
letra_negativa = frase[-2]
print(letra_negativa)
#Para borrar variables o elementos de una lista
del letra
del lista2[1]
#Para comprobar si un elemento pertenece a una lista
pertenece = 1 in lista2
print(pertenece)
no_pertenece = 2 in lista2
print(no_pertenece)
