# Listas de nombres y edades
nombres = ["Luis", "Maria", "Juan", "Laura"]
edades  = [20, 23, 30, 35]

# Inicializar el diccionario vacío
datos = {}

# Usar un bucle para llenar el diccionario
for i in range(len(nombres)):
    datos[nombres[i]] = edades[i]

# Imprimir el diccionario
print("Datos:", datos)

