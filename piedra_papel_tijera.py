import random

def jugar_piedra_papel_tijeras():
    # Opciones disponibles
    opciones = ['piedra', 'papel', 'tijeras']

    # Solicitar la elección del usuario
    eleccion_usuario = input("Elige piedra, papel o tijeras: ").lower()

    # Validar la elección del usuario
    if eleccion_usuario not in opciones:
        print("Elección no válida. Por favor, elige piedra, papel o tijeras.")
        return

    # Elección de la computadora
    eleccion_computadora = random.choice(opciones)
    print(f"La computadora eligió: {eleccion_computadora}")

    # Determinar el ganador
    if eleccion_usuario == eleccion_computadora:
        print("¡Es un empate!")
    elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijeras') or \
         (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or \
         (eleccion_usuario == 'tijeras' and eleccion_computadora == 'papel'):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

# Ejecutar el juego
jugar_piedra_papel_tijeras()