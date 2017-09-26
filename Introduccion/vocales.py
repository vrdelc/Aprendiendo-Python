#Creamos la cadena de las vocales
vocales = "aeiou"
#Generamos una lista a partir de la cadena
lista = list(vocales)
#Recorremos cada letra de la lista
for letra in lista:
    #Convertimos la letra a mayúscula
    letra_mayus = letra.upper()
    #Lo imprimos
    print(letra_mayus)
#También se podría hacer sin convertir la cadena a lista, ya que recorre cada carácter
