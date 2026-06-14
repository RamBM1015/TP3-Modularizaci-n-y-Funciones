# main.py
from logica_mision import (
    calcular_combustible,
    configurar_nave,
    obtener_coordenadas,
    registrar_tripulantes
)

if __name__ == "__main__":
    # Configuración de la nave usando argumentos por nombre en distinto orden
    configurar_nave(estado="Listo para despegar", nombre="Odisea")

    # Calcular combustible
    distancia = 150
    consumo = 2
    print(f"Combustible necesario: {calcular_combustible(distancia, consumo)} litros")

    # Obtener coordenadas y desempaquetar
    x, y, z = obtener_coordenadas()
    print(f"Coordenadas actuales -> X: {x}, Y: {y}, Z: {z}")

    # Registrar tripulantes
    registrar_tripulantes("Alice", "Bob", "Carlos", "Diana")

"""
Disculpeme Profe, lo hice con ia ;(
"""
