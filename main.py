from tablero import Tablero
from algoritmos import Solucionador
from vista import MostrarCamino

def ejecutar ():
    libre = "⬜"
    ruta = "◾"
    inicio = "✅"
    destino = "❌"
    caracter_edificio = "🏨"
    caracter_agua = "♒"
    porcentaje_agua = 4
    dimension_min = 5
    caracter_obstaculo = "🚫"

    print("-- Bienvenido a la ciudad --")
    while True:
        try:
            dimension = int(input(f"*Dime el tamaño de la ciudad. OBS('El tamaño debe ser mayor a {dimension_min}!'): "))
            if dimension <= dimension_min:
                print(f"El valor debe ser mayor a {dimension_min}, ajustamos a un valor por defecto!")
                dimension = dimension_min
            break
        except ValueError:
            print("Favor solo ingresar numeros!")

    tablero = Tablero(dimension, caracter_edificio, caracter_agua, porcentaje_agua, libre, inicio, destino)
    tablero.mostrar() 
    print("\n-- Configuremos tu Destino --\n")

    while True:
        try:
            fila_entrada = int(input("Dime la fila del punto de partida: "))
            columna_entrada = int(input("Dime la columna del punto de partida: "))
            entrada = (fila_entrada, columna_entrada)

            if not (0 <= fila_entrada < dimension and 0 <= columna_entrada < dimension):
                print(f"Este punto esta fuera de la ciudad {fila_entrada,columna_entrada}")
            elif tablero[fila_entrada][columna_entrada] == caracter_edificio:
                print(f"Aqui no puedes colocar ya que hay un edificio {fila_entrada, columna_entrada}")
            elif tablero[fila_entrada][columna_entrada] == caracter_agua:
                print(f"Aqui no puedes colocar, hay un rio {fila_entrada, columna_entrada}")
            else:
                print(f"Colocaste el punto de partida en la posicion {fila_entrada, columna_entrada}")
                break
        except ValueError:
            print("Favor solo ingrese numeros")

    while True:
        try:
            fila_salida = int(input("Dime la fila del punto de llegada: "))
            columna_salida = int(input("Dime la columna del punto de llegada: "))
            salida = (fila_salida, columna_salida)

            if not (0 <= fila_salida < dimension and 0 <= columna_salida < dimension):
                print(f"Este punto esta fuera de la ciudad {fila_salida,columna_salida}")
            elif tablero[fila_salida][columna_salida] == caracter_edificio:
                print(f"Aqui no puedes colocar ya que hay un edificio {fila_salida, columna_salida}")
            elif tablero[fila_salida][columna_salida] == caracter_agua:
                print(f"Aqui no puedes colocar, hay un rio {fila_salida, columna_salida}")
            elif salida == entrada:
                print(f"Estas colocando en el mismo punto de inicio {fila_salida, columna_salida}")
            else:
                print(f"Colocaste el punto de llegada en la posicion {fila_salida, columna_salida}\n")
                break
        except ValueError:
            print("Favor solo ingrese numeros")

    tablero.modificar(entrada, salida)
    tablero.mostrar()
    
    obstaculo_opcional = [] 