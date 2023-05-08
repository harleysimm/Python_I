lista_nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking',
                 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

magos_list = ['Harry Houdini', 'David Blaine', 'Teller']

cientificos_list = [lista_nombres[1], lista_nombres[3], lista_nombres[6]]

otros_list = [elemento for elemento in lista_nombres
                if elemento not in magos_list and elemento not in cientificos_list]

def hacer_grandioso():
    for mago in magos_list:
        print(f'El gran {mago}')


def imprimir_nombres():
    for elemento in lista_nombres:
        print(elemento)

print('\n-------------------------------------------------\n')
print('Todos los nombres:')
imprimir_nombres()
print('\n-------------------------------------------------\n')
print('Magos grandiosos:')
hacer_grandioso()
print('\n-------------------------------------------------\n')
print('Científicos:')
for cientifico in cientificos_list:
    print(cientifico)
print('\n-------------------------------------------------\n')
print('Restantes:')
for restantes in otros_list:
    print(restantes)
print('\n-------------------------------------------------\n')




