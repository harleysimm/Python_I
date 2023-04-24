# 5. Escriba un programa que elimine un signo de exclamación del final de una cadena. 
# puede suponer que los datos de entrada son siempre una cadena, no es necesario verificarlos.

# def eliminar_exclamación (texto):
texto = str(input('Ingrese un texto exclamativo (por ejemplo hola!): '))
if texto.endswith('!'):
    print(texto[:-1])
