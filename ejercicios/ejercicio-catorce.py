# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
# Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
# y en función de su respuesta le muestre un menú con los ingredientes disponibles
# para que elija. Solo se puede eligir un ingrediente además de la mozzarella 
# y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla 
# si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

pizza_vegetariana = ['- Pimiento', '- Tofu']
pizza_normal = ['- Peperoni', '- Jamon', '- Salmon']
base_pizza = ['- Tomate', '- Mozarella']

print('\n-----------------------------------------\n')
print('****** Bienvenido a la Pizzeria Bella Napoli ******')
print('\n-----------------------------------------\n')
print('Nuestros ingredientes base son:')
for base in base_pizza:
    print(base)

tipo_pizza = str(input("¿Qué tipo de pizza quiere hoy? (Vegetariana/Normal): "))
print('\n-----------------------------------------\n')

if tipo_pizza == 'vegetariana':
        print('Los ingredientes vegetarianos son: ')
        for vegetariana in pizza_vegetariana:
            print(vegetariana)
        
        ingrediente = str(input("¿Qué ingrediente vegetariano desea para su pizza?: "))
else:
        print('Los ingredientes normales son: ')
        for normal in pizza_normal:
            print(normal)

        ingrediente = str(input("¿Qué ingrediente normal desea para su pizza?: "))

print('\n-----------------------------------------\n')
print(f'La pizza seleccionada es {tipo_pizza} y tiene los siguientes ingredientes tomate, mozarella y {ingrediente}')
print('Por favor pase por caja, ¡Gracias por su preferencia! ')
print('\n-----------------------------------------\n')