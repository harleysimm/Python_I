class Droid:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

android = Droid('Arturo')

print(android.name)

## Cree una clase llamada Artefacto, agreguele tres atributos y 
## utilice los getter and setter para acceder a ellos

class Artefacto:
    def __init__(self, marca, capacidad, temperatura):
        self.__marca = marca
        self.__capacidad = capacidad
        self.__temperatura = temperatura

    @property
    def marca(self) -> str:
        return self.__marca
    
    @marca.setter
    def marca(self, marca: str) -> None:
        self.__marca = marca
    
    @property
    def capacidad(self) -> float:
        return self.__capacidad
    
    @capacidad.setter
    def capacidad(self, capacidad: str) -> None:
        self.__capacidad = capacidad
    
    @property
    def temperatura(self) -> int:
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, temperatura: str) -> None:
        self.__temperatura = temperatura


hervidor = Artefacto('Midea', 1.7, 100)
hervidor.color = 'rojo'

print(hervidor.capacidad)


