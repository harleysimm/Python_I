# 3. Escriba un programa que calcule el máximo común divisor entre dos números enteros.
# DIVISORES EN COMUN DE CADA UNO

a = int(input('Ingrese primer número: '))
b = int(input('Ingrese segundo número: '))

a = abs(a)
b = abs(b)
if b > a:
    a, b = b, a
while b:
    a, b = b, a % b

print("El máximo común divisor es", a)


