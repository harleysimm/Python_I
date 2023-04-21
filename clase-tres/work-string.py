first_name= "Soledad"
last_name = "Infante"
print(first_name + " " + last_name)

mensaje1 = "Hola " * 3
print(mensaje1)

mensaje3 = "Sebastián"
print(mensaje3)
mensaje3 += ","
print(mensaje3)
mensaje3 += " Castro"
print(mensaje3)

print(len(mensaje3))

cadena = "esto es una oración por Ucrania"
posicion =cadena.find("pelo")
print("pelo se encuentra en: ", posicion)
cadena1 = "esto es una oración por Ucrania"
posicion =cadena1.find("Ucrania")
print("Ucrania se encuentra en: ", posicion)

# Lower 

string = "ALARMA"
print(string.lower())

#Como reemplazar cadenas

string2 = "Hola Hola Chao Hola"
print(string2.replace("Chao", "Hola"))

empty_list = []
print(empty_list)

fullfiled_list = [1, 3, 500, 1.4, [2, "a"], {"name": "Sebastian"}, (1, 3, 5)]
print(fullfiled_list)

second_list = list()
print(second_list)

print(list("Concurso"))

range_one = range(50)
print(list(range_one))

numeros = [1, 4, 6]
print(numeros)
numeros.append(10)
print(numeros)

print(numeros[2])

lista = ['palabra1', 'palabra2', 'palabra3']
#forma 1
for i in range(len(lista)):print(lista[i])
#forma 2
for i in lista:
    print(i)

# Tenemos la siguiente lista
mi_lista = [0 , 1 , 2 , 3 , 4 , 5]

 # Utilizamos pop , asignandolo a una variable . Eliminamos el 5
elemento_eliminado = mi_lista.pop(2)
#  # Pero tambien podemos no asignarlo . Eliminamos el 4
# mi_lista.pop()
# Imprimimos
print(mi_lista)
print(elemento_eliminado)

#remove(e): elimina el elemento e de la lista. Si e no existe en la lista, obtendremos un ValueError.
lista2 = [1 , 2 , 3 , 4]
lista2.remove(1)
print (lista2)

#modificar posición de la lista
lista3 = [2, 4, 7]
lista3 [2] = 6
print(lista3)

#Tuplas
empty_tuple = ()
print(empty_tuple)
fullfiled_tuple = (1, "Rafael", 3.1416)
print(fullfiled_tuple)
one_tuple = ('Gabriela',)
print(type(one_tuple))

hojas = 'carta', 'oficio'
print(type(hojas))
print(hojas)

list_to_convert = [2, 6, 8, 9]
print(list_to_convert)

tuple_converted = tuple(list_to_convert)
print(tuple_converted)

#reverse(): nos permite invertir los elementos de la lista.
lista4 = [1 , 2 , 3 , 4 , 5]
lista4.reverse()
print(lista4)

# #extend(): este metodo tambien nos permite agregar elementos a la lista, pero a diferencia del metodo append,
# pasamos como argumento algo que podemos recorrer (como por ejemplo otra lista), agregando cada uno de
# los elementos.
listax = [1 , 2 , 3 , 4]
print (listax)
listay = [5 , 6 , 7]
listax.extend(listay)
print(listax)
listax.extend([8 , 9])
print(listax)

#remove(e): elimina el elemento e de la lista. Si e no existe en la lista, obtendremos un ValueError.
listaz = [1 , 2 , 3 , 4]
listaz.remove(3)
print(listaz)

thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple)

#sort The sort() method sorts the list ascendingby default.
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

#the clear method removes all the elements from a list
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()



