peso_payaso = 112
peso_munieca = 75

num_payasos = int(input('Ingrese número de payasos a enviar: '))
num_muniecas = int(input('Ingrese número de muñecas a enviar: '))

peso_total = (num_payasos * peso_payaso) + (num_muniecas * peso_munieca)
print(f'El peso total del paquete es: {peso_total} grms.')