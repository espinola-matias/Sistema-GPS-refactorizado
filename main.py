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