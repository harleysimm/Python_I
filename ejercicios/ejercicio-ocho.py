interes = 0.04
monto_inicial = float(input('Ingrese monto inicial para su cuenta de ahorros en dolares:'))

saldo_anio1 = monto_inicial + (monto_inicial * interes)
saldo_anio2 = saldo_anio1 + (saldo_anio1 * interes)
saldo_anio3 = saldo_anio2 + (saldo_anio2 * interes)

print(f'La cantidad de ahorros tras el primer año son {round(saldo_anio1, 2)} dolares')
print(f'La cantidad de ahorros tras el segundo año son {round(saldo_anio2, 2)} dolares')
print(f'La cantidad de ahorros tras el tercer año son {round(saldo_anio3, 2)} dolares')
