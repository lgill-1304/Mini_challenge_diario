# Solicita al usuario que ingrese una lista de números separados por espacios
entrada = input("Ingreses una lista de numeros sparados por espacios: ")

# Convierte la entrada en una lista de números enteros
numeros = list(map(int, entrada.split()))

# Ordena la lista de números en orden ascendente
numeros_ordenados = sorted(numeros)

# Imprime la lista ordenada
print("Lista ordenada:", numeros_ordenados)
