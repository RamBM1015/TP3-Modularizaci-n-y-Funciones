# logica_mision.py

def calcular_combustible(distancia, consumo_por_km):
    """
    Calcula el combustible necesario.
    Retorna distancia * consumo_por_km.
    """
    return distancia * consumo_por_km


def configurar_nave(nombre, modelo="Explorador", estado="Óptimo"):
    """
    Configura la nave con nombre, modelo y estado.
    Usa valores por defecto si no se pasan.
    """
    print(f"Nave configurada: Nombre={nombre}, Modelo={modelo}, Estado={estado}")


def obtener_coordenadas():
    """
    Retorna una tupla con coordenadas (x, y, z).
    """
    x, y, z = 120, 45, 300  # valores de ejemplo
    return (x, y, z)


def registrar_tripulantes(*args):
    """
    Registra una cantidad variable de tripulantes.
    """
    print("Tripulantes a bordo:")
    for tripulante in args:
        print(f"- {tripulante}")
