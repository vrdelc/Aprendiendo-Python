# Programación orientada a objetos en ![Python](https://techspawn.com/wp-content/uploads/2016/10/Python_logo.png)

A continuación se muestra una explicación acerca de la programación orientada a objetos en Python. Para ver ejemplos, [main.py](https://github.com/vrdelc/Aprendiendo-Python/tree/master/Orientado%a%objetos/main.py) instancia las clases y utiliza sus métodos, [tablero.py](https://github.com/vrdelc/Aprendiendo-Python/tree/master/Orientado%a%objetos/tablero.py) y [jugador.py](https://github.com/vrdelc/Aprendiendo-Python/tree/master/Orientado%a%objetos/jugador.py) tienen clases para ser utilizadas.
## Creación de clases
Para definir una clase sólo hay que utilizar ***class nombre_clase:*** y a continuación los atributos, constructor y métodos
## Atributos
Los atributos son variables que tiene la clase y a los que se puede acceder poniendo ***objeto.atributo***
IMPORTANTE: cualquier objeto definido al prinicipio se puede acceder con ***self.atributo*** y si se utiliza esta estructura para cualquier variable, se convierte en atributo y puede ser tratada igual.
## Constructor
Es el método que es llamado para crear un objeto de esa clase, sin parámetros es ***def __init__(self):*** seguido de los atributos que queramos iniciar. En caso de pasar parámetros ***def __init__(self, param1, param2):*** y si quisiéramos que uno de esos parámetros no fuera obligatorio le ponemos un valor por defecto, ***def __init__(self, param1="hola", param2=4):*** .
También se pueden crear objetos a partir de diccionarios para ello el constructor sería ***def __init__(self, \*\*kwargs):***  , para obtener luego los valores tenemos que usar ***kwargs.get(etiqueta)*** y si quisiéramos que hubiera valores por defecto que no sean necesarios introducir, ***kwargs.get(etiqueta, valor)***
## Instanciar objetos
Para instanciar un objeto sin parámetros sólo tenemos que asignar a una variable así ***objeto = Clase()*** , si tuviera parámetros se añaden en el paréntesis ***objeto = Clase("hola", 3)*** .
En caso de que sea a partir de un diccionario ***objeto = Clase(etiqueta1 ="hola", etiqueta2=4)***
## Métodos
Para definirlos, ***def metodo(self):*** y si quisiéramos pasar parámetros como en el constructor  ***def metodo(self, param1, param2):***
## Impresión de datos
Este método se llama automáticamente al imprimir un objeto y se define ***def __str__(self): *** y se utiliza return seguido de la cadena a imprimir.
## Herencia
Para que una clase herede de otra al definirla la nombramos Para definir una clase sólo hay que utilizar ***class nombre_hijo(nombre_padre):*** . Todos los atributos y métodos que tenga el padre y volvamos a crear se sobreesribirán.