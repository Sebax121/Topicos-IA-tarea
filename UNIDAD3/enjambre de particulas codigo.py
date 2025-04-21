import random


# MÉTODO PARA CREAR E INICIALIZAR UNA PARTÍCULA

class Particula:
    def __init__(self, dim, bounds):
        # Posición aleatoria dentro de los límites
        self.posicion = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
        # Velocidad aleatoria proporcional al rango
        self.velocidad = [random.uniform(-abs(bounds[i][1] - bounds[i][0]), abs(bounds[i][1] - bounds[i][0])) for i in range(dim)]
        # Guarda su mejor posición conocida
        self.mejor_posicion = list(self.posicion)
        self.valor_mejor = float('inf')


    # MÉTODO PARA EVALUAR LA PARTÍCULA
    def evaluar(self, funcion_objetivo):
        valor_actual = funcion_objetivo(self.posicion)
        if valor_actual < self.valor_mejor:
            self.valor_mejor = valor_actual
            self.mejor_posicion = list(self.posicion)
    # MÉTODO PARA MOVER LA PARTÍCULA

    def mover(self, mejor_global, w=0.5, c1=1.5, c2=1.5):
        for i in range(len(self.posicion)):
            r1 = random.random()
            r2 = random.random()
            # Fórmula de actualización de velocidad y posición
            self.velocidad[i] = (w * self.velocidad[i] +
                                 c1 * r1 * (self.mejor_posicion[i] - self.posicion[i]) +
                                 c2 * r2 * (mejor_global[i] - self.posicion[i]))
            self.posicion[i] += self.velocidad[i]


# MÉTODO PARA CREAR E INICIALIZAR TODO EL ENJAMBRE

def crear_enjambre(num_particulas, dim, bounds):
    return [Particula(dim, bounds) for _ in range(num_particulas)]


# MÉTODO PARA EVALUAR TODO EL ENJAMBRE

def evaluar_enjambre(enjambre, funcion_objetivo):
    for particula in enjambre:
        particula.evaluar(funcion_objetivo)


# MÉTODO PARA MOVER TODO EL ENJAMBRE

def mover_enjambre(enjambre, mejor_global):
    for particula in enjambre:
        particula.mover(mejor_global)


# FUNCIÓN OBJETIVO (Ejemplo: Esfera)

def funcion_esfera(posicion):
    return sum(x**2 for x in posicion)


# FUNCIÓN PRINCIPAL (main)

def main():
    dimensiones = 2                          # Número de variables
    limites = [(-10, 10)] * dimensiones      # Límites para cada dimensión
    num_particulas = 20                      # Tamaño del enjambre
    iteraciones = 50                         # Número de iteraciones

    # Crear enjambre
    enjambre = crear_enjambre(num_particulas, dimensiones, limites)

    mejor_global = None
    valor_mejor_global = float('inf')

    # Ciclo principal de PSO
    for iteracion in range(iteraciones):
        evaluar_enjambre(enjambre, funcion_esfera)

        for particula in enjambre:
            if particula.valor_mejor < valor_mejor_global:
                valor_mejor_global = particula.valor_mejor
                mejor_global = list(particula.mejor_posicion)

        mover_enjambre(enjambre, mejor_global)

        print(f"Iteración {iteracion+1} - Mejor valor global: {valor_mejor_global:.4f}")

    print("\n🔍 Mejor solución encontrada:", mejor_global)
    print("🎯 Valor óptimo:", valor_mejor_global)


# EJECUCIÓN DEL PROGRAMA

if __name__ == "__main__":
    main()
