cantidad = int(input("Ingrese la cantidad de dinero a invertir: "))
intereses = float(input("Ingrese el interés: "))
anios = int(input("Ingrese el número de años: "))

capital = cantidad * (1 + (intereses/100))**anios
print(f"El capital obtenido en la inversión es {round(capital, 2)} dolares")
