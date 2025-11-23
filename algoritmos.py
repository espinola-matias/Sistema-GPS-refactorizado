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

            if 0 <= nueva_fila < self.dimension and 0 <= nueva_columna < self.dimension:
                vecino = (nueva_fila, nueva_columna)
                contenido_celda = self.tablero[nueva_fila][nueva_columna]
                if vecino in self.obstaculos_opcionales:
                    continue 
        
                if contenido_celda == self.edificio:
                    continue 

                # verificamos la celda con agua en caso de permitir el paso agregamos a la lista y si no ignoramos
                elif contenido_celda == self.agua:
                    if permitir_agua:
                        movimientos_validos.append((vecino, self.costo_agua))
                    else:
                        continue
                # devolvemos camino con costos normales para bfs
                else:
                    movimientos_validos.append((vecino, self.costo_normal))

        return movimientos_validos
    
class Solucionador:
    def __init__(self, tablero, caracter_edificio, caracter_agua, obstaculos_opcional, dimension):
        self.tablero = tablero
        self.edificio = caracter_edificio
        self.agua = caracter_agua
        self.obstaculos = obstaculos_opcional
        self.dimension = dimension

    def resolver_con(self, algoritmo_nombre, inicio, destino):
        servicio_vecinos = ObtenerVecinos(self.tablero, self.dimension, self.edificio, self.agua, self.obstaculos)
        # obtenemos los movimientos y inicializamos en none la estrategia porque aun no esta definida
        estrategia = None

        if algoritmo_nombre == "BFS":
            print(f"\nBusqueda con Algoritmo BFS (No podemos pasar por ninguna obstruccion)")
            estrategia = EstrategiaBFS(servicio_vecinos)
            
        elif algoritmo_nombre == "A_Star":
            print("\nBusqueda con Algoritmo A* (Podemos pasar los Rios pero no obstaculos!)")
            estrategia = EstrategiaAStar(servicio_vecinos)
        
        else:
            print("Error algoritmo no reconocido")
            return None

        return estrategia.resolver(inicio, destino)
    
    class EstrategiaAStar:
        def __init__(self, obtener_vecinos_service):
            self.vecinos_service = obtener_vecinos_service

        # Vemos la distancia de Manhattan
        def heuristica(self, a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        def resolver(self, inicio, destino):
            # guardo la cola de prioridad y pasos y usamos para elegir el camino con menor costo
            contador_pasos = 0
            cola = []
            heapq.heappush(cola, (0, contador_pasos, inicio))
            # Diccionario padre, para saber de donde vino para reconstruir
            padre = {inicio: None}
            
            # Diccionario para llevar la cuenta del costo del recorrido
            costo_recorrido = {inicio: 0}