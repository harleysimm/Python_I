class Vehicle:
    def __init__(self, brand, type):
        self.brand = brand
        self.type = type

Skoda = Vehicle('Yeti', 'SUV')
print(Skoda.type)
Skoda.type = 'Sedan'
print(Skoda.type)

print('\n---------------------------------------------\n')

class Droid:
    def __init__(self, name):
        self.hidden_name = name

    @property
    def name(self) -> str:
        return self.hidden_name
    
    @name.setter
    def name(self, name: str) -> None:
        self.hidden_name = name

android = Droid('arthur')

print(android.name)
android.name = 'Citripio'
print(android.name)

android.hidden_name = 'Rojo'
print(android.hidden_name)

print(android.name)

print('\n---------------------------------------------\n')

class CalculatedValue:
    def __init__(self, name, height):
        self.name = name
        self.heigth = height

    @property
    def get_calculated_value(self) -> float: #los valores calculados jamás reciben parametros
        return 0.35 * self.heigth
    
valuex = CalculatedValue('ratio', 10)

print(f'El {valuex.name} es: {valuex.get_calculated_value}')

#los atributos de los objetos solo viven en el objeto creado (particular)
#los atributos de clase pertenecen solo a la clase (son globales)

print('\n---------------------------------------------\n')

class Dog:
    obeys_owner = True

    def __init__(self, name): #constructor
        self.name = name

dog_one =Dog('Robin')
dog_two =Dog('Malta')
dog_three =Dog('Luz')

print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owner}')

print('\n---------------------------------------------\n')

dog_one.obeys_owner = False
dog_two.obeys_owner=False
print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owner}')

print('\n---------------------------------------------\n')

del dog_one.obeys_owner
# Dog.obeys_owner = True
print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owner}')

print('\n---------------------------------------------\n')