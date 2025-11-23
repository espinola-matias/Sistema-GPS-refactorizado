class MostrarCamino:
    def __init__(self, tablero, camino, entrada, salida, ruta, inicio, destino, dimension_min):
        self.tablero = tablero
        self.camino = camino
        self.entrada = entrada
        self.salida = salida
        self.ruta = ruta
        self.inicio = inicio
        self.destino = destino
        self.dimension_min = dimension_min

    def mostrar_camino(self):
        ciudad_con_camino = [fila [:] for fila in self.tablero] # Realizo la copia del tablero para poder mostrar el camino si hay 

        if self.camino:
            for fila, columna in self.camino:
                if (fila, columna) != self.entrada and (fila, columna) != self.salida:
                    ciudad_con_camino[fila][columna] = self.ruta

        #Realizo una sobre posicion de entrada y salida en caso de algun error y no marque 
        ciudad_con_camino[self.entrada[0]][self.entrada[1]] = self.inicio
        ciudad_con_camino[self.salida[0]][self.salida[1]] = self.destino