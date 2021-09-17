import pygame
import math
import random

pygame.init()

from main import TARGET

l = int(math.sqrt(len(TARGET)))
WIDTH  = 100 * l
HEIGHT =  100 * l
W_SIZE = (WIDTH,HEIGHT)

BLACK = (0,0,0)
WHITE = (255,255,255)

done = False

screen = pygame.display.set_mode(W_SIZE)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    for x in range(100,WIDTH, 100):
        pygame.draw.line(screen, BLACK,(x, 0), (x,HEIGHT), 2)
    for y in range(100, HEIGHT, 100):
        pygame.draw.line(screen, BLACK,(0, y), (WIDTH, y), 2)
    pygame.display.flip()
