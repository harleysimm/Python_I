#Dado un capital K a un interés Y (que oscila entre 0 y 100) durante Z años se desea saber en cuanto se habrá covertido ese capital en Z años, sabiendo que es acumulativo.
# Capital = K
# Interes = Y 
# Años = Z

K = int(input("Ingrese su capital inicial: "))
Z = int(input("Ingrese la cantidad de años: "))
Y = 1.5

años = range (Z)
I = Y / 100

for elemento in años:
    K = K * (1 + I)
print(f"El capital final ganado a {Z} años con un interés del 1.5 es: {K}")
