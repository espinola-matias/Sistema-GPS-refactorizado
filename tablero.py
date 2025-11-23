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

    def __getitem__(self, index):
        return self.tablero[index]
    
    def generar_tablero(self):
        for fila in range(0, self.dimension, 2):
            for columna in range(0, self.dimension, 2):
                self.tablero[fila][columna] = self.edificio

        for fila in range(self.dimension):
            for columna in range(self.dimension):
                if self.tablero[fila][columna] == self.camino:
                    if random.randint(0, 100) <= self.porcentaje:
                        self.tablero[fila][columna] = self.agua