import random
# Número de individuos en cada generación
POPULATION_SIZE = 100

#Genes válidos
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

# Cadena de destino que se generará
TARGET = "Me encantan la I.A."

class Individual(object):
    '''
    Clase que representa al individuo en la población
    '''
    def __init__(self, chromosome):
        self.chromosome = chromosome 
        self.fitness = self.cal_fitness()
  
    @classmethod
    def mutated_genes(self):
        '''
        crear genes aleatorios para la mutación
        '''
        global GENES
        gene = random.choice(GENES)
        return gene
  
    @classmethod
    def create_gnome(self):
        '''
        crear un cromosoma o cadena de genes
        '''
        global TARGET
        gnome_len = len(TARGET)
        return [self.mutated_genes() for _ in range(gnome_len)]
  
    def mate(self, par2):
        '''
        Realizar apareamiento y producir nueva descendencia
        '''
  
        # cromosoma para la descendencia
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):    
  
            # probabilidad aleatoria
            prob = random.random()
  
            # si prob es menor que 0.45, insertar gen
            # del padre 1 
            if prob < 0.45:
                child_chromosome.append(gp1)
  
            # si prob esta entre 0.45 y 0.90, insertar gen
            # del padre 2
            elif prob < 0.90:
                child_chromosome.append(gp2)
  
            # de lo contrario, insertar un gen aleatorio (mutado),
            # para mantener la diversidad
            else:
                child_chromosome.append(self.mutated_genes())
  
        # crear un nuevo individuo (descendencia) usando
        # cromosoma generado para la descendencia
        return Individual(child_chromosome)
  
    def cal_fitness(self):
        '''
        Calcular la puntuación de aptitud, es el número de caracteres 
        en la cadena origen que difieren de la cadena de destino
        '''
        global TARGET
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET):
            if gs != gt: fitness+= 1
        return fitness


# Código principal
def main():
    global POPULATION_SIZE
  
    #la generación actual
    generation = 1
  
    found = False
    population = []
  
    # crear población inicial
    for _ in range(POPULATION_SIZE):
                gnome = Individual.create_gnome()
                population.append(Individual(gnome))
  
    while not found:
  
        # ordenar la población en orden creciente de puntuación de aptitud física
        population = sorted(population, key = lambda x:x.fitness)
  
        # si el individuo alcanza el puntaje de aptitud más bajo, es decir.
        # 0 entonces sabemos que hemos llegado al objetivo
        # y romper el bucle
        if population[0].fitness <= 0:
            found = True
            break
  
        # De lo contrario, se generan nuevos descendientes para la nueva generación
        new_generation = []
  
        # Realizar elitismo, lo que significa que el 10% de la población más apta
        # pasa a la siguiente generación
        s = int((10*POPULATION_SIZE)/100)
        new_generation.extend(population[:s])
  
        # Del 50% de la población más apta, los individuos
        # se aparearán para producir descendencia
        s = int((90*POPULATION_SIZE)/100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)
  
        population = new_generation
  
        print("Generación: {}\tString: {}\tFitness: {}".\
              format(generation,
              "".join(population[0].chromosome),
              population[0].fitness))
  
        generation += 1
  
      
    print("Generación: {}\tString: {}\tFitness: {}".\
          format(generation,
          "".join(population[0].chromosome),
          population[0].fitness))


main()