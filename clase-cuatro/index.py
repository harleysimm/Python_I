print("======== Trabajando con dicccionarios =======")

empty_dict = {}

fullfiled_dict = {
    "id": 1,
    "name": "Gabriela"
}

print(empty_dict)
print(fullfiled_dict)

print("======== Ejercicio dos =======================")

lista_1 = ['a1', 'b2']
dict_converted = dict(lista_1)
print(lista_1, dict_converted)

tupla_1 = ('a1', 'b2')
print(tupla_1, dict(tupla_1))

list_dimensional = [['a', 1], ['b', 3]]
print(list_dimensional, dict(list_dimensional))


empty_dict_2 = dict()
print(empty_dict_2)

full_dict = dict(
    genero = "M",
    nacionalidad = "E"
)
print(full_dict)


empleado = {
    "name": "valeria",
    "apellido": "roso",
    "edad": 18,
    "rut": "11.111.111-1"
}

print(empleado)
for variablex in empleado.values():
    print(variablex)

print(empleado)
for clave, valor in empleado.items():
    print(clave, valor)



print("======== Trabajando con condicionales =======")

edad = 60
if edad > 50:
    print("Hola Don")
    print("Hola desde adentro de if")


print("aca continua el codigo")

# Esto es un comentario

temperatura = 38
if temperatura >= 37:
    print("Alerta de temperatura alta")
else:
    print("La temperatura aun es normal")

temperatura = 5
pais = 'Chile'

if temperatura < 10:
    if pais == 'chile':
        print('cccc')
    else:
        print('zzzz')
else:
    if pais == 'chile':
        print('111')
    else:
        print('222')

if temperatura < 10:
    print("Es altamente probable que nieve")
elif temperatura >= 10 and temperatura <= 20:
    print("Es medianamente probable que nieva")
else:
    print("No hay posibilidad de nieve")


print("======== Trabajando con ciclos =======")
print("=============== WHILE 1================")
print("======== Trabajando con ciclos =======")

want_exit = 'n'
while want_exit == 'n':
    print("Hola como estas?")
    want_exit = input("¿Quieres Salir S/N?")
print("Fuera del while")



print("======== Trabajando con ciclos =======")
print("=============== WHILE 2================")
print("======== Trabajando con ciclos =======")
# break, nos permite romper un ciclo
want_exit = 'n'
num_questions = 0
while want_exit == 'n':
    print("Hola como estas?")
    want_exit = input("¿Quieres Salir S/N?")
    num_questions += 1
    if num_questions == 4:
        print("Alcanzaste el maximo permitido")
        break
print("se acabo el while")





   


