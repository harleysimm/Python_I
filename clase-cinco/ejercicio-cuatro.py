# 4. Dado un mes como un número entero del 1 al 12, 
# devuelva a qué trimestre del año pertenece como un número entero.
# Por ejemplo: el mes 2 (febrero), forma parte del primer trimestre; el mes 6 (junio), 
# forma parte del segundo trimestre; y el mes 11 (noviembre), forma parte del cuarto trimestre.}

# Se pide el mes 
mes = int(input('Ingrese el mes a consultar (como número del 1 al 12) : '))
if 1 > mes > 12:
    print('El valor ingresado no es válido')

# # Se devuelve el trimestre correspondiente al mes 
if mes >= 1 and mes <= 3:
    print('Corresponde al trimestre 1')
elif mes > 3 and mes <= 6:
    print('Corresponde al trimestre 2')
elif mes > 6 and mes <= 9:
    print('Corresponde al trimestre 3')
elif mes > 9 and mes <= 12:
    print('Corresponde al trimestre 4')