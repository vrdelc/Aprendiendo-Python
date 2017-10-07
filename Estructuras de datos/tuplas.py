#Las tuplas son inmutables, no se pueden cambiar
tupla = (1, 2, 3, 4, 5)
print("Creación de la tupla: "+ str(tupla))
tupla_2 = 1, 2, 3, 4, 5
print("Creación de la tupla sin paréntesis: "+ str(tupla_2))
#Tupla de un sólo elemento
tupla_3 = (1,)
print("Tupla de un elemento: "+ str(tupla_3))
#Acceso a los elementos
elemento = tupla[2]
print("Elemento de una tupla: "+ str(elemento))
#En caso de tener listas en las tuplas, ellas son mutables
tupla_4 = (1, "hola", [1,2,3,4])
print("Tupla con lista: "+ str(tupla_4))
tupla_4[2][3] = 6
print("Tupla con lista cambiada: "+ str(tupla_4))
del tupla_4[2][1]
print("Tupla con lista cambiada: "+ str(tupla_4))
