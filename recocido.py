import random
import math
import time

def evaluar_tablero(solucion):
    """ Calcula el número de conflictos en el tablero """
    conflictos = 0
    n = len(solucion)

    for i in range(n):
        for j in range(i + 1, n):
            if solucion[i] == solucion[j] or abs(solucion[i] - solucion[j]) == abs(i - j):
                conflictos += 1

    return conflictos

def generar_vecino(solucion):
    """ Genera una nueva solución modificando una reina al azar """
    vecino = solucion[:]
    i = random.randint(0, 7)
    nuevo_valor = random.randint(0, 7)
    vecino[i] = nuevo_valor
    return vecino

def recocido_simulado(solucion_inicial, temperatura_inicial, temperatura_minima, enfriamiento, max_iter):
    """ Algoritmo de Recocido Simulado """
    solucion = solucion_inicial[:]
    temperatura = temperatura_inicial
    conflictos_actual = evaluar_tablero(solucion)
    
    for iteracion in range(max_iter):
        vecino = generar_vecino(solucion)
        conflictos_vecino = evaluar_tablero(vecino)

        # Si la nueva solución es mejor, la aceptamos
        if conflictos_vecino < conflictos_actual:
            solucion = vecino
            conflictos_actual = conflictos_vecino
        else:
            # Aceptamos soluciones peores con cierta probabilidad
            probabilidad = math.exp((conflictos_actual - conflictos_vecino) / temperatura)
            if random.random() < probabilidad:
                solucion = vecino
                conflictos_actual = conflictos_vecino

        # Reducimos la temperatura
        temperatura *= enfriamiento

        # Mostrar progreso cada 100 iteraciones
        if iteracion % 100 == 0:
            print(f"Iteración {iteracion}, Temperatura {temperatura:.3f}, Mejor evaluación {conflictos_actual}")

        # Si encontramos una solución sin conflictos, terminamos
        if conflictos_actual == 0:
            break

    return solucion, conflictos_actual

# -------------------------------
# 🔹 Parámetros del Recocido Simulado
# -------------------------------
temperatura_inicial = 10000  # Alta temperatura inicial
temperatura_minima = 0.001   # Temperatura final
enfriamiento = 0.99          # Enfriamiento más lento
max_iter = 2000              # Más iteraciones

# -------------------------------
# 🔹 Ejecución múltiple para encontrar la mejor solución
# -------------------------------
mejor_solucion = None
mejor_conflictos = float("inf")
tiempo_inicio = time.time()

for intento in range(10):  # Ejecutamos el algoritmo 10 veces
    solucion_inicial = [random.randint(0, 7) for _ in range(8)]  # Generamos una solución aleatoria
    solucion, conflictos = recocido_simulado(solucion_inicial, temperatura_inicial, temperatura_minima, enfriamiento, max_iter)

    if conflictos < mejor_conflictos:
        mejor_conflictos = conflictos
        mejor_solucion = solucion

    print(f"🔹 Intento {intento + 1}: Conflictos restantes = {conflictos}")

# -------------------------------
# 🔹 Resultado final
# -------------------------------
tiempo_total = time.time() - tiempo_inicio

print("\n✅ Mejor solución encontrada:", mejor_solucion)
print("✅ Conflictos restantes:", mejor_conflictos)
print(f"⏱️ Tiempo total: {tiempo_total:.5f} segundos")
import random
import math
import time

def evaluar_tablero(solucion):
    """ Calcula el número de conflictos en el tablero """
    conflictos = 0
    n = len(solucion)

    for i in range(n):
        for j in range(i + 1, n):
            if solucion[i] == solucion[j] or abs(solucion[i] - solucion[j]) == abs(i - j):
                conflictos += 1

    return conflictos

def generar_vecino(solucion):
    """ Genera una nueva solución modificando una reina al azar """
    vecino = solucion[:]
    i = random.randint(0, 7)
    nuevo_valor = random.randint(0, 7)
    vecino[i] = nuevo_valor
    return vecino

def recocido_simulado(solucion_inicial, temperatura_inicial, temperatura_minima, enfriamiento, max_iter):
    """ Algoritmo de Recocido Simulado """
    solucion = solucion_inicial[:]
    temperatura = temperatura_inicial
    conflictos_actual = evaluar_tablero(solucion)
    
    for iteracion in range(max_iter):
        vecino = generar_vecino(solucion)
        conflictos_vecino = evaluar_tablero(vecino)

        # Si la nueva solución es mejor, la aceptamos
        if conflictos_vecino < conflictos_actual:
            solucion = vecino
            conflictos_actual = conflictos_vecino
        else:
            # Aceptamos soluciones peores con cierta probabilidad
            probabilidad = math.exp((conflictos_actual - conflictos_vecino) / temperatura)
            if random.random() < probabilidad:
                solucion = vecino
                conflictos_actual = conflictos_vecino

        # Reducimos la temperatura
        temperatura *= enfriamiento

        # Mostrar progreso cada 100 iteraciones
        if iteracion % 100 == 0:
            print(f"Iteración {iteracion}, Temperatura {temperatura:.3f}, Mejor evaluación {conflictos_actual}")

        # Si encontramos una solución sin conflictos, terminamos
        if conflictos_actual == 0:
            break

    return solucion, conflictos_actual

# -------------------------------
# 🔹 Parámetros del Recocido Simulado
# -------------------------------
temperatura_inicial = 10000  # Alta temperatura inicial
temperatura_minima = 0.001   # Temperatura final
enfriamiento = 0.99          # Enfriamiento más lento
max_iter = 2000              # Más iteraciones

# -------------------------------
# 🔹 Ejecución múltiple para encontrar la mejor solución
# -------------------------------
mejor_solucion = None
mejor_conflictos = float("inf")
tiempo_inicio = time.time()

for intento in range(10):  # Ejecutamos el algoritmo 10 veces
    solucion_inicial = [random.randint(0, 7) for _ in range(8)]  # Generamos una solución aleatoria
    solucion, conflictos = recocido_simulado(solucion_inicial, temperatura_inicial, temperatura_minima, enfriamiento, max_iter)

    if conflictos < mejor_conflictos:
        mejor_conflictos = conflictos
        mejor_solucion = solucion

    print(f"🔹 Intento {intento + 1}: Conflictos restantes = {conflictos}")

# -------------------------------
# 🔹 Resultado final
# -------------------------------
tiempo_total = time.time() - tiempo_inicio

print("\n✅ Mejor solución encontrada:", mejor_solucion)
print("✅ Conflictos restantes:", mejor_conflictos)
print(f"⏱️ Tiempo total: {tiempo_total:.5f} segundos")
