import random

# ✅ Función objetivo a minimizar (función de esfera)
def funcion_objetivo(x):
    return sum([xi**2 for xi in x])

# 🧩 Clase que representa una partícula individual
class Particula:
    def __init__(self, dimension, limites):
        self.posicion = [random.uniform(limites[i][0], limites[i][1]) for i in range(dimension)]
        self.velocidad = [random.uniform(-1, 1) for _ in range(dimension)]
        self.mejor_posicion = self.posicion[:]
        self.mejor_valor = funcion_objetivo(self.posicion)

    def actualizar_velocidad(self, mejor_global, w=0.5, c1=1.5, c2=1.5):
        for i in range(len(self.velocidad)):
            r1 = random.random()
            r2 = random.random()
            cognitivo = c1 * r1 * (self.mejor_posicion[i] - self.posicion[i])
            social = c2 * r2 * (mejor_global[i] - self.posicion[i])
            self.velocidad[i] = w * self.velocidad[i] + cognitivo + social

    def mover(self, limites):
        self.posicion = [self.posicion[i] + self.velocidad[i] for i in range(len(self.posicion))]
        for i in range(len(self.posicion)):
            if self.posicion[i] < limites[i][0]:
                self.posicion[i] = limites[i][0]
            elif self.posicion[i] > limites[i][1]:
                self.posicion[i] = limites[i][1]
        valor_actual = funcion_objetivo(self.posicion)
        if valor_actual < self.mejor_valor:
            self.mejor_valor = valor_actual
            self.mejor_posicion = self.posicion[:]

# 🚀 Función principal del algoritmo PSO
def pso(dimension, limites, num_particulas=30, iteraciones=100):
    enjambre = [Particula(dimension, limites) for _ in range(num_particulas)]
    mejor_global = enjambre[0].mejor_posicion[:]
    mejor_valor_global = funcion_objetivo(mejor_global)

    for _ in range(iteraciones):
        for particula in enjambre:
            particula.actualizar_velocidad(mejor_global)
            particula.mover(limites)
            valor_particula = funcion_objetivo(particula.posicion)
            if valor_particula < mejor_valor_global:
                mejor_valor_global = valor_particula
                mejor_global = particula.posicion[:]
    
    return mejor_global, mejor_valor_global

# 🧪 Ejecución del algoritmo
if __name__ == "__main__":
    dimension = 2
    limites = [(-10, 10)] * dimension
    mejor_solucion, mejor_valor = pso(dimension, limites, num_particulas=30, iteraciones=100)
    print("Mejor solución encontrada:", mejor_solucion)
    print("Valor de la función objetivo:", mejor_valor)
