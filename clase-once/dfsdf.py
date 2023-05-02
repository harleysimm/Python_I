class Micro():
     
    def __init__(self):
        self.patentes = [] 
        self.ingresos = [] 
        self.tipo_pasajero = ({
            'adulto': 730,
            'adulto_mayor': 730 / 2,
            'niño': 0
        })

    def ingreso_pasajero(self, tipo_pasajero, patente):
        self.patentes.append({
            'patente': patente,
            'tipo_pasajero': tipo_pasajero,
            'correlativo_mvto': 0,
            'tarifa': self.tipo_pasajero[tipo_pasajero]
        })

    def agregar_ingresos_for(self, patente, fecha, tipo_pasajero):
        for movimiento in self.patentes:
            if movimiento['patente'] == patente:
                movimiento['tarifa'] = self.tipo_pasajero[tipo_pasajero]
                movimiento['correlativo_mvto'] += 1
                self.ingresos.append({
                    'patente': patente,
                    'correlativo_mvto': movimiento['correlativo_mvto'],
                    'fecha': fecha,
                    'tipo_pasajero': tipo_pasajero,
                    'valor_pago': movimiento['tarifa']
                })
                break

    def reporte_diario(self, patente):
        ingresos_pasajeros = list(filter(lambda movimientos: movimientos['patente'] == patente, self.ingresos))
        print('{:<15}'.format('N° Mvto.'), '{:<15}'.format('Patente'), '{:<15}'.format('Fecha'), '{:<15}'.format('Tipo Pasajero'), '{:<15}'.format('Valor Pago'))
        for movimiento in ingresos_pasajeros:
            print('{:<15}'.format(movimiento['correlativo_mvto']), '{:<15}'.format(movimiento['patente']), '{:<15}'.format(movimiento['fecha']), '{:<15}'.format(movimiento['tipo_pasajero']), '{:<15}'.format(movimiento['valor_pago']))
