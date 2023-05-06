cantidad = int(input("Introduzca la cantidad de dinero a invertir: "))
intereses = float(input("Introduzca el interés: "))
años = int(input("Introduzca el número de años: "))

capital = cantidad * años * intereses
print(f"El capital obtenido en la inversión es {int(capital)}")
