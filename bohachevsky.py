import numpy as np

# --- 1. CONFIGURACIÓN DE PARÁMETROS ---
POP_SIZE = 50           # Tamaño de la población
GENERATIONS = 100       # Número de iteraciones
MUTATION_RATE = 0.15    # Probabilidad de que un gen mute (15%)
MUTATION_SIGMA = 0.05   # Fuerza de la mutación (Ajustado para el dominio estrecho)
DOMAIN_MIN = -1.0
DOMAIN_MAX = 1.0

# --- 2. FUNCIONES MATEMÁTICAS ---
def bohachevsky(ind):
    """Evalúa la función de Bohachevsky 1 para un individuo [x, y]."""
    x, y = ind[0], ind[1]
    return (x**2) + 2*(y**2) - 0.3*np.cos(3*np.pi*x) - 0.4*np.cos(4*np.pi*y) + 0.7

def calculate_fitness(population):
    """Calcula el fitness de toda la población. (Maximizamos 1 / (1 + f(x,y)))"""
    fitness = np.zeros(POP_SIZE)
    for i in range(POP_SIZE):
        # Evitamos divisiones por cero en caso extremo sumando un epsilon muy pequeño si se desea, 
        # pero f(x,y) de Bohachevsky siempre es >= 0, así que el denominador >= 1.
        fitness[i] = 1.0 / (1.0 + bohachevsky(population[i]))
    return fitness

# --- 3. OPERADORES GENÉTICOS ---
def tournament_selection(population, fitness, k=3):
    """Selección por torneo: elige k individuos al azar y devuelve el mejor."""
    selected_indices = np.random.choice(POP_SIZE, k, replace=False)
    best_index = selected_indices[np.argmax(fitness[selected_indices])]
    return population[best_index]

def arithmetic_crossover(parent1, parent2):
    """Cruce aritmético: crea hijos promediando los genes de los padres."""
    alpha = np.random.rand()
    child1 = alpha * parent1 + (1 - alpha) * parent2
    child2 = (1 - alpha) * parent1 + alpha * parent2
    return child1, child2

def mutate(individual):
    """Mutación gaussiana con control de fronteras (Clamping)."""
    for i in range(2): # Iteramos sobre x e y
        if np.random.rand() < MUTATION_RATE:
            # Añadimos ruido gaussiano
            individual[i] += np.random.normal(0, MUTATION_SIGMA)
            
    # Control de fronteras estricto para mantenerlos en [-1, 1]
    return np.clip(individual, DOMAIN_MIN, DOMAIN_MAX)

# --- 4. BUCLE PRINCIPAL DEL ALGORITMO ---
def run_genetic_algorithm():
    # Inicialización Uniforme en [-1, 1]
    population = np.random.uniform(DOMAIN_MIN, DOMAIN_MAX, (POP_SIZE, 2))
    
    print("Iniciando evolución...\n")
    
    for gen in range(GENERATIONS):
        fitness = calculate_fitness(population)
        
        # Elitismo: Encontrar y guardar al mejor individuo para no perderlo
        best_idx = np.argmax(fitness)
        best_ind = population[best_idx]
        best_val = bohachevsky(best_ind)
        
        # Imprimir progreso cada 10 generaciones
        if gen % 10 == 0 or gen == GENERATIONS - 1:
            print(f"Generación {gen:3d} | Mejor f(x,y): {best_val:.6f} | Coordenadas: x={best_ind[0]:.5f}, y={best_ind[1]:.5f}")
        
        # Construir la nueva generación
        new_population = [best_ind.copy()] # Arrancamos con el élite
        
        while len(new_population) < POP_SIZE:
            # 1. Selección
            p1 = tournament_selection(population, fitness)
            p2 = tournament_selection(population, fitness)
            
            # 2. Cruce
            c1, c2 = arithmetic_crossover(p1, p2)
            
            # 3. Mutación y Clamping
            c1 = mutate(c1)
            c2 = mutate(c2)
            
            new_population.extend([c1, c2])
            
        # Asegurar que la población tenga el tamaño exacto (por si se pasó al añadir de a dos)
        population = np.array(new_population[:POP_SIZE])

    print("\nEvolución terminada.")
    print(f"Mínimo global encontrado: f(x,y) = {best_val:.8f}")
    print(f"En las coordenadas: x = {best_ind[0]:.8f}, y = {best_ind[1]:.8f}")

# Ejecutar el script
if __name__ == "__main__":
    run_genetic_algorithm()