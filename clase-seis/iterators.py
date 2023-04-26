words = 'Esto es una cadena de letras'

for letter in words:
    print(letter)


cadena = 'Esto es una cadena de texto '

word = ''
for letter in cadena:
    if letter != ' ':
        word += letter
    else:
        print(word)
        word = ''
print('\n-----------------------------------\n')

for letter in cadena:
    if letter != ' ' :
        print(letter)
    else:
        break
print('\n-----------------------------------\n')

animals_list = ['Gato', 'Perro', 'Ardilla']
for animal in animals_list:
    print(animal)

print('\n-----------------------------------\n')

list1 = range(2,3)
print(list1)
for number_in in range(1, 10):
    print(number_in)
print('\n-----------------------------------\n')
for number_in in range(1, 10, 2): #el dos representa la distancia
    print(number_in)

print('\n---------------Tlabas de multiplicar--------------------\n')
for num_tabla in range(1, 11):
    for num_mul in range(1, 11):
        result = num_tabla * num_mul
        print(f'{num_tabla} x {num_mul} = {result}')
    print('\n-----------------------------------\n')

print('\n------------Arreglos bidimensionales-----------------------\n')
double_list = [[1, 2, 3],[4, 6, 7]]

print(double_list[0])
print(double_list[1])

print(double_list[0][2])
print(double_list[1][1])