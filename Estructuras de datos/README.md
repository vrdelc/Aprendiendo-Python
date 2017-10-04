# Estructuras de datos en
![Python](https://techspawn.com/wp-content/uploads/2016/10/Python_logo.png)
En esta parte trataremos ciertas estructuras de datos importantes para el desarrollo en python.

## 1. Listas

## 2. Tuplas

## 3. Conjuntos

## 4. Diccionarios

## 5. Slices
Nos permiten obtener trozos de una lista o una cadena de texto. Su estructura es la siguiente: ***lista[inicio:fin]***, donde tanto el inicio es un índice incluido y el fin no. Se pueden utilizar números negativos como en las listas y no es necesario poner uno de loos dos datos, entonces seleccionaría hasta el principio o final, y si sólo está así ***lista[:]*** toda la lista.
Otra posible estructura es la siguiente: ***lista[inicio:fin:salto]***, que nos dice cada cuantas posiciones escoger en la seleccion. Se puede dejar en blanco, o utilizar números negativos.
Para borrar cualquier elemento de la lista o un conjunto de ellos pondremos delante ***del*** y para hacer reemplazos, utilizaremos la primera estructura de inicio:fin y le asignaremos con el igual una nueva lista que se añadirá en esas posiciones.
Para ver estas ideas con ejemplos, revisar el fichero [slices.py](https://github.com/vrdelc/Aprendiendo-Python/tree/master/Estructuras%20de%20datos/slices.py)
