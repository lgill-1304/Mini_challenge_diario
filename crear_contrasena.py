import random
import string

def generar_contraseña():
    # Pedir al usuario la longitud de la contraseña
    while True:
        try:
            longitud = int(input("Introduce la longitud de la contraseña (entre 8 y 16 caracteres): "))
            if 8 <= longitud <= 16:
                break
            else:
                print("Por favor, introduce un número entre 8 y 16.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    # Definir los caracteres permitidos
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Generar la contraseña
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

    # Mostrar la contraseña generada
    print(f"Tu contraseña segura es: {contraseña}")

# Ejecutar el generador de contraseñas
generar_contraseña()
