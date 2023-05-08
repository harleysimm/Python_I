edad_minima = 16 
ingresos_tope = 1000

anios = int(input('Cuál es su edad?: '))
ingreso = float(input('Cuál es su ingreso mensual (en euros)?: '))

if anios > edad_minima and ingreso >= ingresos_tope:
    print('Paga impuestos')
else:
    print('No cumple requisitos')

