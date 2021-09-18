import random
import pygame
import math
import time

# GENES = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,20,21,22,23,24,25,26,27,28,29,30]

int TARGET = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
# TARGET = [random.randint(1,Q_GENES) for _ in range(16)]
Q_GENES = 1000
POPULATION_SIZE = 1000
pygame.init()

l = int(math.sqrt(len(TARGET)))

WIDTH  = 100 * l
HEIGHT =  100 * l
W_SIZE = (WIDTH,HEIGHT)

BLACK = (0,0,0)
WHITE = (255,255,255)

done = False

screen = pygame.display.set_mode(W_SIZE)



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
                if TARGET[i] == self.cromosoma[i]:
                    child.append(self.cromosoma[i])
                else:
                    child.append(random.randint(1,Q_GENES))
            else:
                if random.randint(0,1) or TARGET[i] == self.cromosoma[i]:
                    child.append(parent.cromosoma[i])
                else:
                    child.append(random.randint(1,Q_GENES))
        return Sujeto(child)


def generate_population():
    population = []
    for _ in range(POPULATION_SIZE):
        population.append(Sujeto([random.randint(1,Q_GENES) for _ in range(len(TARGET))]))
    return population

def run(population,flag,generacion):
    done = False
    aux = True
    fuente = pygame.font.Font(None,30)

    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    while not done:
        ## PYGAME

        if aux:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            Q_GENES = int(text)
                            aux = False
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            screen.fill((30, 30, 30))
            # Render the current text.
            txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            # Blit the text.
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pygame.draw.rect(screen, color, input_box, 2)

            pygame.display.flip()
            clock.tick(30)
        else:
            if not flag:
                population = sorted(population, key = lambda x:x.puntuacion,reverse=True)
                # for i in population:
                #     print(i.puntuacion,i.cromosoma)
                # flag = True

                #Condición de Parada
                if population[0].puntuacion == len(TARGET):
                    flag = True


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

                # time.sleep(1.5)
                print(f'Generacion: {generacion}, Poblacion: {population[0].cromosoma},Puntuacion: {population[0].puntuacion}')

                generacion += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            screen.fill(WHITE)

            for x in range(100,WIDTH, 100):
                pygame.draw.line(screen, BLACK,(x, 0), (x,HEIGHT), 2)
            for y in range(100, HEIGHT, 100):
                pygame.draw.line(screen, BLACK,(0, y), (WIDTH, y), 2)


            # str(population[0].cromosomas[i])
            i = 0

            # for y in range(50, HEIGHT, 100):
            #     for x in range(50,WIDTH, 100):
            #         texto = fuente.render(str(population[0].cromosoma[int((((x/50)-1)/2)+(l*((y/50)-1)/2))]),0,(200,60,80))
            #         screen.blit(texto,((x,y)))

            # int(population[0].cromosomas[i])

            # int((((x/50)-1)/2)+(l*((y/50)-1)/2))

            for y in range(50, HEIGHT, 100):
                for x in range(50,WIDTH, 100):
                    texto = fuente.render(str(population[0].cromosoma[int((((x/50)-1)/2)+(l*((y/50)-1)/2))]),0,(200,60,80))
                    screen.blit(texto,((x,y)))
        pygame.display.flip()

    print(f'Generacion: {generacion}, Poblacion: {population[0].cromosoma},Puntuacion: {population[0].puntuacion}')

if __name__ == "__main__":
    population = generate_population()
    flag = False
    generacion = 1

    run(population,flag,generacion)
