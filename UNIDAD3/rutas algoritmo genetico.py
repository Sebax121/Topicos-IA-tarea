import random

# Lista de ciudades
cities = [
    "Vigo", "Valladolid", "Bilbao", "Zaragoza", "Gerona", "Barcelona", "Madrid",
    "Badajoz", "Sevilla", "Cádiz", "Jaén", "Granada", "Murcia", "Valencia", "Albacete"
]

# Distancias directas (pueden ser incompletas)
raw_edges = [
    ("Vigo", "Valladolid", 356), ("Vigo", "Bilbao", 577), ("Valladolid", "Bilbao", 285),
    ("Bilbao", "Zaragoza", 296), ("Zaragoza", "Gerona", 396), ("Gerona", "Barcelona", 100),
    ("Barcelona", "Zaragoza", 298), ("Barcelona", "Valencia", 349), ("Valencia", "Murcia", 241),
    ("Murcia", "Granada", 278), ("Granada", "Jaén", 88), ("Jaén", "Albacete", 258),
    ("Albacete", "Madrid", 251), ("Madrid", "Zaragoza", 325), ("Madrid", "Valladolid", 193),
    ("Madrid", "Badajoz", 403), ("Badajoz", "Sevilla", 218), ("Sevilla", "Cádiz", 125),
    ("Sevilla", "Jaén", 242), ("Albacete", "Valencia", 191), ("Madrid", "Bilbao", 395),
    ("Bilbao", "Barcelona", 610), ("Bilbao", "Valencia", 611), ("Valladolid", "Barcelona", 705),
    ("Sevilla", "Madrid", 528), ("Granada", "Madrid", 423), ("Cádiz", "Madrid", 646),
    ("Murcia", "Madrid", 400)
]

# Crear matriz de distancias (Floyd-Warshall)
INF = float('inf')
dist_matrix = {a: {b: INF for b in cities} for a in cities}
for city in cities:
    dist_matrix[city][city] = 0
for a, b, d in raw_edges:
    dist_matrix[a][b] = d
    dist_matrix[b][a] = d

# Aplicar Floyd-Warshall
for k in cities:
    for i in cities:
        for j in cities:
            if dist_matrix[i][j] > dist_matrix[i][k] + dist_matrix[k][j]:
                dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]

# Calcular distancia total de una ruta con Floyd-Warshall
def route_distance(route):
    total = 0
    for i in range(len(route)):
        a = route[i]
        b = route[(i + 1) % len(route)]  # ciclo cerrado
        d = dist_matrix[a][b]
        if d == INF:
            return INF
        total += d
    return total

# Crear una ruta aleatoria
def random_route():
    r = cities[:]
    random.shuffle(r)
    return r

# Cruzamiento entre dos rutas
def crossover(p1, p2):
    start, end = sorted(random.sample(range(len(p1)), 2))
    child = p1[start:end]
    child += [c for c in p2 if c not in child]
    return child

# Mutación por intercambio
def mutate(route, rate=0.01):
    for i in range(len(route)):
        if random.random() < rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]

# Algoritmo genético
def genetic_algorithm(pop_size=100, generations=500):
    population = [random_route() for _ in range(pop_size)]

    for _ in range(generations):
        population.sort(key=route_distance)
        next_gen = population[:10]  # elitismo
        while len(next_gen) < pop_size:
            p1, p2 = random.sample(population[:50], 2)
            child = crossover(p1, p2)
            mutate(child)
            next_gen.append(child)
        population = next_gen

    best = population[0]
    best_cost = route_distance(best)
    return best, best_cost

# Ejecutar
if __name__ == "__main__":
    best, cost = genetic_algorithm()
    if cost == float('inf'):
        print("⚠ No se encontró una ruta válida.")
    else:
        print("✅ Ruta óptima encontrada:")
        print(" -> ".join(best))
        print(f"🛣 Distancia total: {cost:.2f} km")
