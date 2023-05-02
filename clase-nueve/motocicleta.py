class Motocicleta():
    # Atributos de clase
    is_new = True
    motor = False

    # Métodos constructor sirve solamente para inicializar valores
    def __init__(self, color, matricula, combustible_litros, numero_ruedas,
                 marca, modelo, fecha_fabricacion, velocidad_punta, peso, capacidad_lts):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.capacidad_lts = capacidad_lts

    def arrancar(self):
        if self.motor:
            print("El motor ya ha arrancado")
        else:
            print("El motor ya estaba en marcha")

    def detener(self):
        if self.motor:
            print("Se detiene el motor.")
        else:
            print("El motor ya está detenido")

    def consulta_precio(self):
        if self.consulta_precio:
            print(f'EL precio de la motocicleta {self.marca} {self.modelo} es de {self.precio} ')

    def comprobar_combustible(self):
        print(f'---> Reporte del depósito de la motocicleta {self.marca} {self.modelo} <---')
        print(f'La cantidad de combustible que tiene es de {self.combustible_litros} y su capacidad máxima es de {self.capacidad_lts}')
        print(f'Faltan {self.capacidad_lts - self.combustible_litros} para llenar el tanque')

    def reponer(self):
        while True:
            self.reponer_litros = float(input("Introduzca la cantidad de litros a rellenar:\n"))
            
            if self.combustible_litros + self.reponer_litros <= self.capacidad_lts:
                print(f"Se han llenado {self.reponer_litros} litros.")
                self.combustible_litros += self.reponer_litros 
                print(f"El depósito tiene {self.combustible_litros} litros de combustible.")
                break
            else:
                print("Has excedido el máximo de combustible")


Motorcycle1 = Motocicleta(
    'Verde',
    'XYZ22',
    10,
    2,
    'Kawasaki',
    'Ninja ZX-10R',
    '04/11/2014',
    200,
    170,
    14
)

Motorcycle2 = Motocicleta(
    fecha_fabricacion="03/02/2023",
    matricula="BCD44",
    capacidad_lts=18.9,
    combustible_litros=0,
    color="azul",
    marca="Harley Davidson",
    modelo="Fat Boy 114",
    numero_ruedas=2,
    velocidad_punta=180,
    peso=304
)

# Motorcycle1.arrancar()
# Motorcycle2.arrancar()

# Motorcycle1.precio = 5700000
# Motorcycle1.consulta_precio()

Motorcycle2.comprobar_combustible()

Motorcycle2.reponer()



