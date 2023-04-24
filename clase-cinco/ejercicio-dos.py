# 2. utilizando dos while anidados, construya 
#las tablas de mutiplicacion, ejemplo
#     Ejemplo while anidados:
#     while condicion1
#         while condicion2
#             ..... 
	
def tablas_multlipicar():
    start = 1
    end = 10

    a = start
    while a <= end:
        b = start
        print(f'Tabla de multiplicar del {a}:')        
        while b <= end:
            print(a, '*', b, '=', a*b)
            b += 1
        a += 1
        print()

tablas_multlipicar()

