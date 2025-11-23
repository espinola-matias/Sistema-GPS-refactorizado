import heapq
from collections import deque

class ObtenerVecinos:
    def __init__(self, tablero, dimension, edificio, agua, obstaculos_opcionales):
        self.tablero = tablero
        self.dimension = dimension
        self.edificio = edificio
        self.agua = agua
        self.obstaculos_opcionales = obstaculos_opcionales or []
        # configuracion de costos
        self.costo_normal = 1
        self.costo_agua = 5  # Puede cruzar por el agua pero tiene un costo mayor