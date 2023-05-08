dividendo = int(input('Ingrese un número: '))
divisor = int(input('Ingrese un segundo número: '))

while divisor == 0:
    print('No se puede dividir por cero')
    divisor = int(input('Ingrese nuevo número: '))

resultado = dividendo / divisor
print(round(resultado, 2))
