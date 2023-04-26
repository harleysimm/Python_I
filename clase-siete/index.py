# Creando una clase las clases son unmolde, y esa clase produce objetos
class Transporte:
    pass

#Instanciar la clase y crear un objeto
transporte1 = Transporte()
transporte2 = Transporte()

class BuzzeLightYear:
    pass

bozz1 = BuzzeLightYear()
bozz2 = BuzzeLightYear()

print(type(transporte1))
print(type(bozz1))

class Droid: #declarar clase
    def __init__(self):
        self.power_on = False

    def switch_on(self):  #construir dos métodos, debe incluirse el self en todos los métodos
        print('Hola soy un droid y estoy a tu orden') #todos los atributos de nuestra clase deben ser llamados self
        self.power_on = True

    def switch_off(self):
        print('Adiós, enciéndeme cuando me necesites')
        self.power_on = False

k8_arthur = Droid()
k8_citripio = Droid() #instanciar clase

k8_arthur.switch_on()
print('power on Arthur: ', k8_arthur.power_on)
print('power off Citripio: ', k8_citripio.power_on)
k8_arthur.switch_off()
print(k8_arthur.power_on)

class Vehicle:
    def __init__(self, type, model):
        self.type_vehicle = type
        self.model_vehicle = model

sedan = Vehicle('Sedan', 'Aveo')
print(sedan.type_vehicle, sedan.model_vehicle)
pickup = Vehicle('Pickup', 'Ranger')
print(pickup.type_vehicle, pickup.model_vehicle)
       