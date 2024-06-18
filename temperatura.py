def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de grados Celsius a grados Fahrenheit.
    
    :param celsius: La temperatura en grados Celsius.
    :return: La temperatura en grados Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    # Solicita al usuario que ingrese una temperatura en grados Celsius
    celsius = float(input("Introduce la temperatura en grados Celsius: "))
    
    # Convierte la temperatura a grados Fahrenheit
    fahrenheit = celsius_a_fahrenheit(celsius)
    
    # Muestra el resultado
    print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

# Ejecuta la función principal
if __name__ == "__main__":
    main()