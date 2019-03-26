import sys
import pygame
from pygame.locals import *
from random import randint
import random
import numpy as np

RES_X = 1280
RES_Y = 640
CELL_SIZE = 32
WIDTH = RES_X//CELL_SIZE
HEIGHT = RES_Y//CELL_SIZE
IS_RUNNING = True
BLACK = (0, 0, 0)
ORANGE = (255, 140, 0)
GREEN = (0, 255, 0)
screen = pygame.display.set_mode((RES_X, RES_Y))
CLOCK = pygame.time.Clock()
grid = [[0] * WIDTH for i in range(HEIGHT)]
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
    while i < roads_horizontally:
        y = randint(1, HEIGHT - 2)    
        if(grid[y][0] == 0 and grid[y - 1][0] == 0 and grid[y + 1][0] == 0):
            for x in range(WIDTH):
                grid[y][x] += 1
            garbage_zone_vert += [y + 1, y - 1]
            i += 1
    i = 0
    while i < roads_vertically:  
        x = randint(1, WIDTH - 2) 
        if(grid[0][x] == 0 and grid[0][x - 1] == 0 and grid[0][x + 1] == 0):
            for j in grid:
                j[x] += 2
            garbage_zone_hor += [x + 1, x - 1]
            i += 1
    
    for i in range(randint(6, 20)):
        rand_vert = random.choice(garbage_zone_vert)
        rand_trashcan_vert = randint(0, WIDTH - 1)
        rand_hor = random.choice(garbage_zone_hor)
        rand_trashcan_hor = randint(0, HEIGHT - 1)

        if(grid[rand_vert][rand_trashcan_vert]) == 0:
            grid[rand_vert][rand_trashcan_vert] = 4
        if(grid[rand_trashcan_hor][rand_hor]) == 0:
           grid[rand_trashcan_hor][rand_hor] = 4
        
    
def grid_fill():
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if(grid[i][j] == 0):
                screen.blit(pygame.image.load('sprites/grass.png'), (j*CELL_SIZE, i*CELL_SIZE))
            if(grid[i][j] == 1):
                screen.blit(pygame.image.load('sprites/horizontal_straight_road.png'), (j*CELL_SIZE, i*CELL_SIZE))
            if(grid[i][j] == 2):
                screen.blit(pygame.image.load('sprites/vertical_straight_road.png'), (j*CELL_SIZE, i*CELL_SIZE))
            if(grid[i][j] == 3):
                screen.blit(pygame.image.load('sprites/crossroad.png'), (j*CELL_SIZE, i*CELL_SIZE))
            if(grid[i][j] == 4):
                pygame.draw.rect(screen, ORANGE, pygame.Rect(j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE))


grid_create()
for r in grid:
    print(r)
grid_fill()

while IS_RUNNING:
    CLOCK.tick(2)
    render_window()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


