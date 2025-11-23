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

    def obtener(self, posicion_actual, permitir_agua):
        fila, columna = posicion_actual
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        movimientos_validos = []

        for cambio_fila, cambio_columna in direcciones:
            nueva_fila = fila + cambio_fila
            nueva_columna = columna + cambio_columna