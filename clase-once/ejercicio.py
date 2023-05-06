# Se necesita realizar un programa basado en clases que permita automatizar el torniquete (control de acceso)
# de una micro, de la siguiente manera:

#1 Las personas que abordan la micro son, mujeres, hombres, niños y adulto mayor, 
# de los cuales los niños no pagan y los adultos mayores pagan la tarifa el 50%
#2 El cobro actual de la micro es de 730 pesos
#3 Por lo que necesitamos un reporte de operacion por día y por micro donde
# (cada micro se registra por patente), se listen los tipos de usuario y la cantidad total recaudada por 
#cada una, anexar a este reporte el total por dia
#4. seria interesante que aparte del reporte anterior que es total, 
# tener uno filtrado por dia y otro filtrado por persona
from datetime import datetime
fecha = datetime.today().strftime('%Y-%m-%d')

class Micro():
     
    def __init__(self):
        self.patentes = [] 
        self.ingresos = [] 
        self.tipo_pasajero = ({
            'adulto': 730,
            'adulto mayor': 730 / 2,
            'niño': 0
        })

    def ingreso_buses(self, patente): #guardar cada micro
        self.patentes.append({
            'patente': patente,
            'correlativo_mvto': 1,
        })

    def agregar_ingresos_for(self, patente, tipo_pasajero):
        for movimiento in self.patentes:
            if movimiento ['patente'] == patente:
                movimiento['tarifa'] = self.tipo_pasajero[tipo_pasajero]
                self.ingresos.append({
                    'patente': patente,
                    'correlativo_mvto': movimiento['correlativo_mvto'],
                    'fecha': datetime.today().strftime('%Y-%m-%d'),
                    'tipo_pasajero': tipo_pasajero,
                    'valor_pago': movimiento['tarifa']
                })
                movimiento['valor_pago'] = movimiento['tarifa']
                movimiento['correlativo_mvto'] = movimiento ['correlativo_mvto'] +1 # correlativo de la patente
                break

    def reporte_diario(self, patente):
        ingresos_pasajeros = list(filter(lambda movimientos: movimientos['patente']== patente, self.ingresos))
        total_pagos = sum([movimiento['valor_pago'] for movimiento in ingresos_pasajeros])

        print('{:<15}'.format('N° Mvto.'), '{:<15}'.format('Patente'), '{:<15}'.format('Fecha'),'{:<15}'.format('Tipo Pasajero'), '{:<15}'.format('Valor Pago'))
        for movimiento in ingresos_pasajeros:
            print('{:<15}'.format(movimiento['correlativo_mvto']), '{:<15}'.format(movimiento['patente']),'{:<15}'.format(movimiento['fecha']),'{:<15}'.format(movimiento['tipo_pasajero']),'{:<15}'.format(movimiento['valor_pago']))

        print('\nTotal pagos: {}'.format(total_pagos))

    def reporte_multiple(self, patentes):
        print('{:<15}'.format('N° Mvto.'), '{:<15}'.format('Patente'), '{:<15}'.format('Fecha'),'{:<15}'.format('Tipo Pasajero'), '{:<15}'.format('Valor Pago'))
        total = 0
        for patente in patentes:
            ingresos_pasajeros = list(filter(lambda movimiento: movimiento['patente'] == patente, self.ingresos))
            for movimiento in ingresos_pasajeros:
                print('{:<15}'.format(movimiento['correlativo_mvto']), '{:<15}'.format(movimiento['patente']),'{:<15}'.format(movimiento['fecha']),'{:<15}'.format(movimiento['tipo_pasajero']),'{:<15}'.format(movimiento['valor_pago']))
                total += movimiento['valor_pago']
        print("Total de los pagos: ", total)

    def reporte_pasajero(self, tipo_pasajero):
        ingresos_pasajeros = list(filter(lambda movimientos: movimientos['tipo_pasajero']== tipo_pasajero, self.ingresos))
        total_pagos = sum([movimiento['valor_pago'] for movimiento in ingresos_pasajeros])

        print('{:<15}'.format('N° Mvto.'), '{:<15}'.format('Tipo Pasajero'), '{:<15}'.format('Fecha'),'{:<15}'.format('Patente'), '{:<15}'.format('Valor Pago'))
        for movimiento in ingresos_pasajeros:
            print('{:<15}'.format(movimiento['correlativo_mvto']), '{:<15}'.format(movimiento['tipo_pasajero']),'{:<15}'.format(movimiento['fecha']),'{:<15}'.format(movimiento['patente']),'{:<15}'.format(movimiento['valor_pago']))

        print('\nTotal pagos: {}'.format(total_pagos))

Recorrido_uno = Micro()


Recorrido_uno.ingreso_buses('FLXV33')
Recorrido_uno.ingreso_buses('FLXV49')
Recorrido_uno.ingreso_buses('FLXV87')

Recorrido_uno.agregar_ingresos_for('FLXV33', 'adulto')
Recorrido_uno.agregar_ingresos_for('FLXV33', 'adulto mayor')
Recorrido_uno.agregar_ingresos_for('FLXV33', 'niño')
Recorrido_uno.agregar_ingresos_for('FLXV49', 'adulto')
Recorrido_uno.agregar_ingresos_for('FLXV49', 'adulto mayor')
Recorrido_uno.agregar_ingresos_for('FLXV49', 'adulto')
Recorrido_uno.agregar_ingresos_for('FLXV49', 'adulto')
Recorrido_uno.agregar_ingresos_for('FLXV49', 'adulto mayor')
Recorrido_uno.agregar_ingresos_for('FLXV49', 'niño')
Recorrido_uno.agregar_ingresos_for('FLXV49', 'adulto')
Recorrido_uno.agregar_ingresos_for('FLXV49', 'adulto mayor')
Recorrido_uno.agregar_ingresos_for('FLXV49', 'niño')
Recorrido_uno.agregar_ingresos_for('FLXV49', 'adulto')
Recorrido_uno.agregar_ingresos_for('FLXV49', 'adulto mayor')
Recorrido_uno.agregar_ingresos_for('FLXV49', 'adulto')
Recorrido_uno.agregar_ingresos_for('FLXV49', 'adulto')
Recorrido_uno.agregar_ingresos_for('FLXV49', 'adulto mayor')
Recorrido_uno.agregar_ingresos_for('FLXV87', 'adulto')
Recorrido_uno.agregar_ingresos_for('FLXV87', 'adulto mayor')
Recorrido_uno.agregar_ingresos_for('FLXV87', 'niño')
Recorrido_uno.agregar_ingresos_for('FLXV87', 'adulto')
Recorrido_uno.agregar_ingresos_for('FLXV87', 'adulto mayor')
Recorrido_uno.agregar_ingresos_for('FLXV87', 'adulto')

# Recorrido_uno.reporte_pasajero('adulto')
# Recorrido_uno.reporte_diario('FLXV49')
Recorrido_uno.reporte_multiple(['FLXV87', 'FLXV49', 'FLXV33'])