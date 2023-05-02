# se desea automatizar el cajero de una entidad bancaria, para
# ello se le encomendado
# realizar un programa en python a base de clases
# en la que se pueda crear una cuenta bancaria,
# registrar los movimientos de abono o cargo y además se debe
# pedir un estado de cuenta de la siguiente manera: Movimiento #, tipo de mov, fecha de mov, monto mov, saldo
from datetime import datetime

class CuentaBancaria:

    def __init__(self, nombre_cliente, rut, cuenta):
        self.nombre_cliente = nombre_cliente
        self.rut = rut
        self.cuenta = cuenta
        self.saldo = 0
        self.movimientos = []

    def mostrar_menu(self):
        print('***Bienvenido por favor elija una opción***',
              '\n------------------------------------\n',
              '**********Menú**********',
              '\n------------------------------------\n',
              '''1- Depósito
            2- Giro
            3- Imprimir estado de cuenta
            4- Salir ''')
        opcion = input("Ingrese una opción del menú: ")
        if opcion == "1":
            self.deposito()
        elif opcion == "2":
            self.giro()
        elif opcion == "3":
            self.imprimir_estado_cuenta()
        elif opcion == "4":
            print("Programa finalizado")
        else:
            print("Opción no válida")

    def deposito(self):
        monto = int(input('Ingrese el monto a depositar: '))
        fecha = datetime.today().strftime('%Y-%m-%d')
        self.saldo += monto
        self.movimientos.append(('Depósito', fecha, monto, self.saldo))
        print(f'Se ha depositado {monto} pesos en la cuenta. Nuevo saldo: {self.saldo} pesos.')

    # def giro(self):
    #     monto = float(input('Ingrese el monto a girar: '))
    #     fecha = datetime.today().strftime('%Y-%m-%d')
    #     if monto > self.saldo:
    #         print('Error: Saldo insuficiente')
    #     else:
    #         self.saldo -= monto
    #         self.movimientos.append(('Giro', fecha, monto, self.saldo))
    #         print(
    #             f'Se ha girado {monto} pesos de la cuenta. Nuevo saldo: {self.saldo} pesos.')

    # def ver_saldo(self):
    #     print(f"El saldo de la cuenta es {self.saldo} pesos.")

    # def imprimir_estado_cuenta(self):
    #     print('*** Estado de cuenta ***')
    # for movimiento in self.movimientos:
    #     print(f'{movimiento[0]} | {movimiento[1]} | {movimiento[2]} | Saldo: {movimiento[3]}')

# Creamos la cuenta bancaria
# cuenta1 = CuentaBancaria('Rafael Castro', 26689393-0, 26689393, 5000)

# Imprimimos el estado de cuenta final
# cuenta1.imprimir_estado_cuenta()
