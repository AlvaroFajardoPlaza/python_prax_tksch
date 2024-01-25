# En este documento vamos a crear una clase, con atributos privados, para practicar con los getter y los setter de la misma

class Pelicula():

    def __init__(self, titulo, lanzamiento, duracion= None, genero="sin clasificar"):
        self.__titulo = titulo
        self.__duracion = duracion
        self.__lanzamiento = lanzamiento
        self.__genero = genero
        print("Hemos creado un nuevo objeto de la clase Pelicula()")

    @property
    def titulo_privado(self):
        print("Esto es un GETTER para el titulo")
        return self.__titulo
    
    @titulo_privado.setter
    def titulo_privado(self, newValue):
        print("Esto es el SETTER del título")
        self.__titulo = newValue

    @property
    def genero_privado(self):
        print("GETTER >>> GENERO")
        return self.__genero
    
    @genero_privado.setter
    def genero_privado(self, newValue):
        print("Esto es el SETTER del género")
        self.__genero = newValue

    def mostrar(self):
        print(self)

    def __str__(self):
        return "Has pedido ver la pelicula {}, del año {} y género {}!".format(self.__titulo, self.__lanzamiento, self.__genero)
    
# Vamos a crear una película:
peli_1 = Pelicula("Star Wars", 1989, genero="ciencia-ficcion")
peli_1.mostrar()
# print(peli_1.__titulo) # Esto nos debería de tirar un error

# Si queremos modificar el valor de alguno de los atributos de clase:
peli_1.titulo_privado
peli_1.titulo_privado = "Star Wars I"
peli_1.mostrar()
peli_1.genero_privado = "aventura"
peli_1.mostrar()


