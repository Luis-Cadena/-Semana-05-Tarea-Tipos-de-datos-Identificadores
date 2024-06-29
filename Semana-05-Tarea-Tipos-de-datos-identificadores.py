# Programa para calcular el área de un círculo
# El programa solicita al usuario que ingrese el radio del círculo,
# luego calcula y muestra el área correspondiente.

import math


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
    radio (float): El radio del círculo.

    Devuelve:
    float: El área del círculo.
    """
    area = math.pi * radio ** 2
    return area


def main():
    """
    Función principal del programa. Solicita al usuario el radio del círculo,
    calcula el área y muestra el resultado.
    """
    # Solicita al usuario que ingrese el radio del círculo
    radio_str = input("Introduce el radio del círculo: ")

    # Convierte la entrada a un número de punto flotante
    radio = float(radio_str)

    # Calcula el área del círculo
    area = calcular_area_circulo(radio)

    # Muestra el resultado
    print(f"El área del círculo con radio {radio} es {area:.2f}")


# Llama a la función principal
if __name__ == "__main__":
    main()
