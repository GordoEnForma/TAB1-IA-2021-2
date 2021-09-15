import random

# GENES = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,20,21,22,23,24,25,26,27,28,29,30]

TARGET = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# TARGET = [random.randint(1,30) for _ in range(16)]

POPULATION_SIZE = 1000

class Sujeto(object): # \(^<^)/
    '''
    Clase que representa al individuo en la población
    '''
    def __init__(self, cromosoma):
        self.cromosoma = cromosoma 
        self.puntuacion = self.puntuar()
    def puntuar(self):
        '''
        Calcular la puntuación de aptitud, es el número de caracteres
        en la cadena origen que difieren de la cadena de destino
        '''
        global TARGET
        puntos = 0
        for pos in range(len(TARGET)):
            if TARGET[pos] == self.cromosoma[pos]: puntos+= 1
        return puntos
    def reproduccion(self,parent):
        child = []
        for i in range(len(self.cromosoma)):
            if len(self.cromosoma)/2 <= i:
                if random.randint(0,1):
                    child.append(self.cromosoma[i])
                else:
                    child.append(random.randint(1,30))
            else:
                if random.randint(0,1):
                    child.append(parent.cromosoma[i])
                else:
                    child.append(random.randint(1,30))
        return Sujeto(child)


def generate_population():
    population = []
    for _ in range(POPULATION_SIZE):
        population.append(Sujeto([random.randint(1,30) for _ in range(len(TARGET))]))
    return population


if __name__ == "__main__":
    population = generate_population()
    flag = False
    generacion = 1

    while not flag:
        population = sorted(population, key = lambda x:x.puntuacion,reverse=True)
        # for i in population:
        #     print(i.puntuacion,i.cromosoma)
        # flag = True

        #Condición de Parada
        if population[0].puntuacion == len(TARGET):
            flag = True
            break

        # De lo contrario, se generan nuevos descendientes para la nueva generación
        nueva_cepa = []
        # Realizar elitismo, lo que significa que el 10% de la población más apta
        # pasa a la siguiente generación
        s = int((10*POPULATION_SIZE)/100)
        nueva_cepa.extend(population[:s])

        # Del 50% de la población más apta, los individuos
        # se aparearán para producir descendencia
        s = int((90*POPULATION_SIZE)/100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            # print('Parent 1',parent1.cromosoma,end="\n")
            # print('Parent 2',parent2.cromosoma,end="\n")

            child = parent1.reproduccion(parent2)
            nueva_cepa.append(child)
            

        
        population = nueva_cepa

        print(f'Generacion: {generacion}, Poblacion: {population[0].cromosoma},Puntuacion: {population[0].puntuacion}')
  
        generacion += 1
    print(f'Generacion: {generacion}, Poblacion: {population[0].cromosoma},Puntuacion: {population[0].puntuacion}')
