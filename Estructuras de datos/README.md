# Estructuras de datos en ![Python](https://techspawn.com/wp-content/uploads/2016/10/Python_logo.png)
En esta parte trataremos ciertas estructuras de datos importantes para el desarrollo en python.

## 1. Slices
Nos permiten obtener trozos de una lista o una cadena de texto. Su estructura es la siguiente: ***lista[inicio:fin]*** , donde tanto el inicio es un índice incluido y el fin no. Se pueden utilizar números negativos como en las listas y no es necesario poner uno de loos dos datos, entonces seleccionaría hasta el principio o final, y si sólo está así ***lista[:]*** toda la lista.
Otra posible estructura es la siguiente: ***lista[inicio:fin:salto]*** , que nos dice cada cuantas posiciones escoger en la seleccion. Se puede dejar en blanco, o utilizar números negativos.
Para borrar cualquier elemento de la lista o un conjunto de ellos pondremos delante ***del*** y para hacer reemplazos, utilizaremos la primera estructura de inicio:fin y le asignaremos con el igual una nueva lista que se añadirá en esas posiciones.
Para ver estas ideas con ejemplos, revisar el fichero [slices.py](https://github.com/vrdelc/Aprendiendo-Python/blob/master/Estructuras%20de%20datos/slices.py)

## 2. Diccionarios
Para crear diccionarios, entre corchetes pondremos parejas de datos separadas por comas. Estas parejas de datos se estructuran: ***valor:dato*** . Para acceder a un dato concreto conociendo el valor: ***diccionario[valor]*** .
Otra forma de crear diccionarios es con una lista de listas, así: ***dict([ [valor1, dato1], [valor2, dato2]])***.
Para recorrer los diccionarios con for, nos va pasando por los valores; pero también podemos obtener los valores con el método **values** y los datos con **keys** , en caso de usar **items()** obtenemos tuplas de la forma ***(valor, dato)*** .
Para ver estas ideas con ejemplos, revisar el fichero [diccionarios.py](https://github.com/vrdelc/Aprendiendo-Python/blob/master/Estructuras%20de%20datos/diccionarios.py)

## 3. Tuplas
Son inmutables, es decir, no se pueden borrar sus elementos ni cambiar. Para crearla: ***(elemento1, elemento2, elemento3)*** o sin paréntesis ***elemento1, elemento2, elemento3*** .En caso de querer crear una tupla de un elemento, habrá que poner una coma detrás del elemento aunque no vay nada detrás. Y para acceder a los elementos ***tupla[posicion]*** .
Aunque sea inmutable, si tenemos una lista en una de las posiciones la podemos editar o borrar sus elementos, siempre que por lo menos quede un elemento.
Para ver estas ideas con ejemplos, revisar el fichero [tuplas.py](https://github.com/vrdelc/Aprendiendo-Python/blob/master/Estructuras%20de%20datos/tuplas.py)

## 4. Conjuntos


## Lista de compras
En este ejercicio se solicita realizar un programa que: agregue artículos, borrar artículos y mostrar artículos. Puedes ver una posible solución en [lista_compra.py](https://github.com/vrdelc/Aprendiendo-Python/blob/master/Estructuras%20de%20datos/lista_compra.py)

## Agenda telefónica
En este ejercicio se solicita realizar un programa que simule una agenda telefónica, con las siguientes funciones: añadir nuevos contactos, borrar contactos, ver todos los contactos, ver un contacto y actualizar un contacto. Puedes ver una posible solución en [agenda_telefonica.py](https://github.com/vrdelc/Aprendiendo-Python/blob/master/Estructuras%20de%20datos/agenda_telefonica.py)
