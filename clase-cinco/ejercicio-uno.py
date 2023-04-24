# 1. Cree un programa que encuentre el promedio de los tres puntajes dados y devuelva el valor de la letra 
# asociada con esa calificación. con al siguiente tabla
#     0   - 2     D
#     2.1 - 5     C
#     5.1 - 6     B
#     6.1 - 7     A

# Se piden los valores
n1 = float(input('Ingrese la nota 1: '))
n2 = float(input('Ingrese la nota 2: '))
n3 = float(input('Ingrese la nota 3: '))
# Se calcula el promedio
promedio = (n1 + n2 + n3) / 3
# # Se devuelve el valor como letra
if promedio >= 0 and promedio <= 2:
    print('D')
elif promedio > 2 and promedio <= 5:
    print('C')
elif promedio > 5 and promedio <= 6:
    print('B')
elif promedio > 6 and promedio <= 7:
    print('A')