"""
Este es un fichero de prueba para poder comprender como podemos crear copias de una variable y de un objeto.

Si queremos hacer una copia de una variable tendremos que emplear el método copy() o bien emplear slicing[:]

Si queremos hacer una copia de un objeto o instancia de clase tendremos que emplear el método copy.deepcopy() o 'copia profunda'.

De esta manera evitaremos la problemática de las referencias.
"""

# Creamos una lista de números sencilla y creamos una copia
import copy 

lista_a = [8,5,6,7]

# Al hacer esto, lista_b y lista_a referencian a lo mismo, pero no estamos creando una copia
lista_b = lista_a
lista_a is lista_b # True

# Podemos crear una copia de esta manera
lista_b = copy.copy(lista_a) # tenemos que importar el método copy
lista_b.append(12)
print("Esta es mi primera lista:", lista_a)
print("\nEsta es mi copia:", lista_b)

# también podemos crear una copia de nuestra lista_a mediante el slicing
lista_c = lista_a[:]
print(lista_c is lista_a) # False

# Vamos a crear ahora una copia de nuestro primer objeto
objeto1 = { "name": "Álvaro", "age":25, "city": "Albacete", "pet":"Nebraska"}
for i, value in enumerate(objeto1):
    print(i, "--->", value, "-->", objeto1.values)

objeto2 = copy.deepcopy(objeto1)
objeto2.update({"comida": "sushi"})
print(objeto1 is objeto2)
print(objeto2)