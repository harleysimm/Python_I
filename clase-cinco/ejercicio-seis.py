# 6. Se le asignado un tarea para programar un algoritmo para una lavadora, 
# debe investigar cuanta agua se necesita para lavar prendas
# con las siguientes caracteriticas, algodon, nilon, poliester, 
# debe investigar para una lavadora de xx kg cuantas prendas de cada una puede 
# lavar entendiendo, que solo se puede lavar ropa de un mismo tipo y asi poder calcular lo siguiente
# Por ejemplo, si la carga es 10, la cantidad de agua que requiere es 5 y la cantidad de ropa a lavar es 14, 
# entonces necesitas 5 * 1.1 ^ (14 - 10) cantidad de agua.

# Escribe una función para calcular cuánta agua se necesita si tienes una cantidad de ropa.
# La función aceptará 2 argumentos: - carga lavadora y ropa. 

# algodon,
# nilon, 
# poliester
# una lavadora de xx kg cuantas prendas de cada una puede lavar
# si lavadora es de 10 kg, la cantidad de agua que requiere es 5 litros y la cantidad de ropa a lavar es 14 prendas


def calcular_agua():

# Definimos tipo de tela
# Se usó un peso aproximado por prenda: 200 grms para algodón, 300 grms para poliester y 50 grms para nylon según información buscada en internet.

    tipo_tela = input('Ingrese tipo de tela (algodon, poliester o nylon): ')
    cantidad_maxima = {'algodon': 50, 'poliester': 33, 'nylon': 200}
    if tipo_tela not in cantidad_maxima:
        return 'Tipo de tela no corresponde'
 
#Definimos capacidad de la lavadora
    capacidad = 10

# Pedimos la cantidad de prendas a lavar
    cantidad = int(input('Ingrese la cantidad de prendas a lavar: '))
    if cantidad > cantidad_maxima[tipo_tela]:
        return 'La cantidad de prendas a lavar es mayor a la capacidad de la lavadora'

    # Calculamos la cantidad de agua necesaria
    agua_base = cantidad_maxima[tipo_tela] * 1.1 ** (cantidad - capacidad)
    agua_total = agua_base * cantidad / capacidad

    return f"Para lavar {cantidad} prendas de {tipo_tela} en una lavadora de {capacidad} kg, se necesitan {agua_total} litros de agua"

    calcular_agua()