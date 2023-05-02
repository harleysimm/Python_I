class Banco:
    cuentas = [] #guardar las cuentas y correlativos
    movimientos = [] #guardar los movimientos

    def __init__(self):
        pass

    def agregar_cuenta(self, cuenta, rut):
        self.cuentas.append({
            'numero_cuenta': cuenta,
            'rut': rut, 
            'correlativo_movimiento': 1, 
            'saldo': 0
        })
        
    def agregar_movimiento_for(self, cuenta, fecha, tipo, monto):#con el for buscamos la cuenta en el recorrido
        for elemento in self.cuentas: #esta variable recibe cada uno de los elementos, recorre elementp a elemento
            if elemento ['numero_cuenta'] == cuenta:
                if tipo == 'Retiro':
                    if elemento ['saldo'] - monto < 0:
                        print('saldo insuficiente')
                else:
                    self.movimientos.append({
                        'numero_cuenta': cuenta,
                        'correlativo_movimiento': elemento ['correlativo_movimiento'],
                        'fecha': fecha,
                        'tipo': tipo,
                        'monto': monto,
                        'saldo': elemento ['saldo'] - monto
                    })
                    elemento['saldo'] = elemento['saldo'] - monto
                    elemento['correlativo_movimiento'] = elemento['correlativo_movimiento'] +1
            else:
                self.movimientos.append({
                    'numero_cuenta': cuenta,
                    'correlativo_movimiento': elemento ['correlativo_movimiento'],
                    'fecha': fecha,
                    'tipo': tipo,
                    'monto': monto,
                    'saldo': elemento ['saldo'] + monto
                })
                elemento['saldo'] = elemento['saldo'] + monto
                elemento['correlativo_movimiento'] = elemento['correlativo_movimiento'] +1
            break

    def estado_cuenta(self, cuenta):
        movimientos_cuenta = list(filter(lambda elementos: elementos['numero_cuenta']== cuenta, self.movimientos))
        print('{:<20}'.format('N° Mvto.'), '{:<20}'.format('Fecha'),'{:<20}'.format('Tipo'), '{:<20}'.format('Monto'),'{:<20}'.format('Saldo'))
        for elemento in movimientos_cuenta:
            print('{:<20}'.format(elemento['correlativo_movimiento']),'{:<20}'.format(elemento['fecha']),'{:<20}'.format(elemento['tipo']),'{:<20}'.format(elemento['monto']),'{:<20}'.format(elemento['saldo']))
        



banco_bci = Banco()

banco_bci.agregar_cuenta("7360001", "14.999.000-1")
banco_bci.agregar_cuenta("7360002", "14.999.000-2")
banco_bci.agregar_cuenta("7360003", "14.999.000-3")
banco_bci.agregar_cuenta("7360004", "15.999.000-4")

banco_bci.agregar_movimiento_for("7360001", "17/04/2023", "Abono", 1000)
banco_bci.agregar_movimiento_for("7360001", "17/04/2023", "Abono", 500)
banco_bci.agregar_movimiento_for("7360001", "17/04/2023", "Retiro", 100)
banco_bci.agregar_movimiento_for("7360001", "17/04/2023", "Abono", 1000)
banco_bci.agregar_movimiento_for("7360001", "17/04/2023", "Retiro", 500)

banco_bci.agregar_movimiento_for("7360002", "17/04/2023", "Abono", 3000)
banco_bci.agregar_movimiento_for("7360002", "17/04/2023", "Abono", 100)
banco_bci.agregar_movimiento_for("7360002", "17/04/2023", "Retiro", 750)

banco_bci.agregar_movimiento_for("7360003", "17/04/2023", "Abono", 5000)

banco_bci.estado_cuenta("7360001")
