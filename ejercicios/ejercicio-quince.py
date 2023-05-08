# inaceptable = 0.0
# aceptable = 0.4
# meritorio = 0.6 o más
dinero_beneficio = 2400

while True:

    puntuacion = float(input('Por favor ingrese el puntaje obtenido en su evaluación: '))
    beneficio = puntuacion * dinero_beneficio

    if puntuacion == 0.0:
        print('Su nivel de rendimiento es INACEPTABLE y no le corresponde beneficio')
        break
    
    elif puntuacion == 0.4:
        print(f'Su nivel de rendimiento es ACEPTABLE y su beneficio es de {int(beneficio)} euros.')
        break

    elif puntuacion >= 0.6:
        print(f'Su nivel de rendimiento es MERITORIO y su beneficio es de {int(beneficio)} euros.')
        break

    else:
        print('Ingrese un puntaje válido')