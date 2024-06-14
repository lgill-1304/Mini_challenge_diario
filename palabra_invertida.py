#Inversion de una Cadena:
#Escribe un programa que invierta una cadena de caracteres dada por el usuario.

def invertir_palabra(cadena_de_palabras):
    if len(cadena_de_palabras) == 0:
        return ""
    else:
        return cadena_de_palabras[-1] + invertir_palabra(cadena_de_palabras[:-1])

resultado = invertir_palabra('Laura')
print(resultado)