def saludar(name):
    print(f'Hola {name} !!!')

def saludar_dos(first_name, last_name):
    print(f'Hola {first_name}, {last_name}!!!')

def multiplicar_texto(texto, multiplier = 2):
    print(texto * multiplier)

def  varieltal(param1, param2, *others):
    print(param1)
    print(param2)
    print(others)

def varieltal_dos(param1, **others):
    print(param1)
    print(others)
    

saludar('Sebastián')
saludar ('Soledad')

saludar_dos(last_name= 'Castro', first_name='Sebastian')

multiplicar_texto('V', 5)

multiplicar_texto('X')

print('\n----------------------------\n')
varieltal('1A', '2B', 0, 'XX', [0, 1])

print('\n----------------------------\n')
varieltal_dos('1A', id = 0, name ='Carlos')