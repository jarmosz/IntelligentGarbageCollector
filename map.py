import sys
import pygame
from pygame.locals import *
from random import randint
import random
import numpy as np

RES_X = 640
RES_Y = 480
CELL_SIZE = 20
WIDTH = RES_X//CELL_SIZE
HEIGHT = RES_Y//CELL_SIZE
IS_RUNNING = True
BLACK = (0, 0, 0)
ORANGE = (255, 140, 0)
GREEN = (0, 255, 0)
SCREEN = pygame.display.set_mode((RES_X, RES_Y))
CLOCK = pygame.time.Clock()
GRID = np.zeros((WIDTH, HEIGHT), dtype='int8')
MIN_ROADS_VERTICALLY = 4
MAX_ROADS_VERTICALLY = 6
MIN_ROADS_HORIZONTALLY = 4
MAX_ROADS_HORIZONTALLY = 6

def render_window():
    pygame.display.update()


def grid_create():
    roads_horizontally = randint(MIN_ROADS_HORIZONTALLY, MAX_ROADS_HORIZONTALLY)
    roads_vertically = randint(MIN_ROADS_VERTICALLY, MAX_ROADS_VERTICALLY)
    garbage_zone_vert = []
    garbage_zone_hor = []
    i = 0
    print('roads x: ' + str(roads_horizontally))
    print('roads y: ' + str(roads_vertically))
    while i < roads_vertically:
        y = randint(1, WIDTH - 2)     
        if(GRID[y, 0] == 0 and GRID[y - 1, 0] == 0 and GRID[y + 1, 0] == 0):
            GRID[y, :] = 1
            garbage_zone_vert += [y + 1, y - 1]
            i += 1
    i = 0
    while i < roads_horizontally:  
        x = randint(1, HEIGHT - 2) 
        if(GRID[0, x] == 0 and GRID[0, x - 1] == 0 and GRID[0, x + 1] == 0):
            GRID[:, x] = 1
            garbage_zone_hor += [x + 1, x - 1]
            i += 1
    for i in range(randint(6, 20)):
        rand_vert = random.choice(garbage_zone_vert)
        rand_trashcan_vert = randint(0, HEIGHT - 1)
        rand_hor = random.choice(garbage_zone_hor)
        rand_trashcan_hor = randint(0, WIDTH - 1)

        if(GRID[rand_vert, rand_trashcan_vert]) == 0:
            GRID[rand_vert, rand_trashcan_vert] = 2
        if(GRID[rand_trashcan_hor, rand_hor]) == 0:
           GRID[rand_trashcan_hor, rand_hor] = 2
        
    
def grid_fill():
    for j in range(HEIGHT):
        for i in range(WIDTH):
            if(GRID[i, j] == 0):
                pygame.draw.rect(SCREEN, GREEN, pygame.Rect(i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            if(GRID[i, j] == 1):
                pygame.draw.rect(SCREEN, BLACK, pygame.Rect(i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            if(GRID[i, j] == 2):
                pygame.draw.rect(SCREEN, ORANGE, pygame.Rect(i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE))

grid_create()
grid_fill()
print(GRID)

while IS_RUNNING:
    CLOCK.tick(2)
    render_window()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


