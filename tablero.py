import random
class Tablero:
    def __init__(self, dimension, edificio, agua, porcentaje, camino, inicio, destino):
        self.dimension = dimension
        self.edificio = edificio
        self.agua = agua
        self.porcentaje = porcentaje
        self.camino = camino
        self.inicio = inicio
        self.destino = destino
        self.tablero = [[ camino for _ in range(dimension)]for _ in range(dimension)]
        self.generar_tablero()