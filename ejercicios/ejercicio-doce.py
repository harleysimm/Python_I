nombre = str(input('Ingrese su nombre: '))
sexo = str(input('Ingrese su sexo (M/H): '))

if (sexo == 'M' and nombre < 'M') or (sexo == "H" and nombre > 'N'):
    grupo = 'A'
else:
    grupo = 'B'

print(f'Te corresponde el grupo {grupo}')