def contar_vocales(cadena):
    # Definir las vocales
    vocales = set ("aeiouAEIOU")
    
    # Inicializar el contador
    contador = 0
    
    # Recorrer cada carácter de la cadena
    for char in cadena:
        # Verificar si el carácter es una vocal
        if char in vocales: 
            # Incrementar el contador si es una vocal
            contador +=1
    
    return contador

cadena = input("Introduce una cadena de texto:")
numero_vocales = contar_vocales(cadena)
print (f"Numero de vocales en la cadena: {numero_vocales}")