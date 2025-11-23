🏙️ Simulador de Rutas Urbanas (Pathfinding City)
Este proyecto es una aplicación de consola interactiva escrita en Python que simula un sistema de navegación en una ciudad generada aleatoriamente. Permite al usuario visualizar y comparar cómo diferentes algoritmos de búsqueda de caminos (Pathfinding) resuelven el problema de ir de un punto A a un punto B evitando obstáculos y ponderando diferentes terrenos.

🚀 Características Principales
Generación Procedural: Cada ejecución crea una ciudad única con edificios (muros) y ríos (terreno costoso).

Múltiples Algoritmos: Implementación de BFS (Breadth-First Search) y *A (A-Star)**.

Sistema de Costos:

🛣️ Tierra: Costo normal.

♒ Agua: Costo elevado (penalización).

Interactividad: El usuario define el tamaño de la ciudad, puntos de inicio/fin y puede agregar obstáculos manuales en tiempo real.

Arquitectura Modular: Código estructurado en módulos separando lógica, vista y modelos.

🧠 Lógica y Algoritmos
El núcleo del proyecto utiliza el Patrón de Diseño Strategy para intercambiar dinámicamente el algoritmo de búsqueda según la elección del usuario.

1. BFS (Búsqueda en Anchura)
Comportamiento: Explora por capas uniformes.

Regla: Considera el agua como un obstáculo infranqueable (Muro).

Uso: Ideal para encontrar el camino más corto en grafos sin pesos.

2. A* (A-Star)
Comportamiento: Utiliza una heurística (Distancia Manhattan) + Costo acumulado para priorizar rutas prometedoras.

Regla: Puede cruzar agua, pero con un costo de movimiento mayor (x5) comparado con la tierra.

Tecnología: Implementado con heapq (Cola de Prioridad) para máxima eficiencia.

🛠️ Tecnologías
Python 3.x

Librerías estándar: collections (deque), heapq, random.

No requiere instalación de librerías externas.

🏁 Cómo ejecutarlo
Clonar el repositorio:

Bash

git clone https://github.com/TU_USUARIO/pathfinding-city.git
cd pathfinding-city
Ejecutar el programa:

Bash

python main.py
Sigue las instrucciones en consola:

Define el tamaño de la ciudad.

Ingresa coordenadas de inicio y fin.

(Opcional) Agrega obstáculos extra.

Elige el algoritmo para ver la magia.

