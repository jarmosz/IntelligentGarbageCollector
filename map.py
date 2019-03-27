import sys
import pygame
from pygame.locals import *
from random import randint
import random
CLOCK_TICK = 30
TRUCK_LEFT = 'sprites/truck_left.png'
TRUCK_TOP = 'sprites/truck_top.png'
TRUCK_RIGHT = 'sprites/truck_right.png'
TRUCK_DOWN = 'sprites/truck_down.png'
EMPTY_TRASH = 'sprites/empty.png'
YELLOW_TRASH = 'sprites/yellow.png'
BLUE_TRASH = 'sprites/blue.jpg'
RED_TRASH = 'sprites/red.png'
RES_X = 1280
RES_Y = 640
CELL_SIZE = 32
WIDTH = RES_X//CELL_SIZE
HEIGHT = RES_Y//CELL_SIZE
IS_RUNNING = True
screen = pygame.display.set_mode((RES_X, RES_Y))
clock = pygame.time.Clock()
grid = [[0] * WIDTH for i in range(HEIGHT)]
MIN_ROADS_VERTICALLY = 4
MAX_ROADS_VERTICALLY = 6
MIN_ROADS_HORIZONTALLY = 4
MAX_ROADS_HORIZONTALLY = 6

truck_offset_x = 0
truck_offset_y = 9
truck_image = TRUCK_LEFT

def render_window():
    grid_fill()
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
            elif(grid[i][j] == 1):
                screen.blit(pygame.image.load('sprites/horizontal_straight_road.png'), (j*CELL_SIZE, i*CELL_SIZE))
            elif(grid[i][j] == 2):
                screen.blit(pygame.image.load('sprites/vertical_straight_road.png'), (j*CELL_SIZE, i*CELL_SIZE))
            elif(grid[i][j] == 3):
                screen.blit(pygame.image.load('sprites/crossroad.png'), (j*CELL_SIZE, i*CELL_SIZE))
            elif(grid[i][j] == 4):
                screen.blit(pygame.image.load(EMPTY_TRASH), (j*CELL_SIZE, i*CELL_SIZE))
            elif(grid[i][j] == 5):
                screen.blit(pygame.image.load(YELLOW_TRASH), (j*CELL_SIZE, i*CELL_SIZE))
            elif(grid[i][j] == 6):
                screen.blit(pygame.image.load(BLUE_TRASH), (j*CELL_SIZE, i*CELL_SIZE))
            elif (grid[i][j] == 7):
                screen.blit(pygame.image.load(RED_TRASH), (j*CELL_SIZE, i*CELL_SIZE))

            if(grid[i][j] == 11 or grid[i][j] == 13 or grid[i][j] == 12):
                screen.blit(pygame.image.load(truck_image), (j*CELL_SIZE+truck_offset_x, i*CELL_SIZE+truck_offset_y))
grid_create()

def can_move_to(tile):
    if tile == 2 or tile == 3 or tile == 1:
        return True
    else:
        return False
    
def move(x,y,i,j):
    x1 = i+x
    y1 = j+y
    if x1<0 or y1<0 or y1>WIDTH-1 or x1>HEIGHT-1:
        return False
    move_to = grid[x1][y1]
    if move_to != 1 and move_to != 2 and move_to != 3:
        return False
    change_truck_sprite(x,y)
    return (x1,y1)

def change_truck_sprite(x,y):
    global truck_image
    global truck_offset_x
    global truck_offset_y
    truck_offset_y=0
    truck_offset_x=0
    if y == 1:
        truck_image = TRUCK_RIGHT
        truck_offset_y = 9
    elif y == -1:
        truck_image = TRUCK_LEFT
        truck_offset_y = 9
    elif x == -1:
        truck_image = TRUCK_TOP
        truck_offset_x = 9
    elif x == 1:
        truck_image = TRUCK_DOWN
        truck_offset_x = 9

def randomize_trashes():
    for i, a in enumerate(grid):
        for j,b in enumerate(a):
            if b == 4:
                grid[i][j] = randint(5,7)
def collect_trash(i,j):
    for x in range(5,8):
        if grid[i+1][j] == x:
            grid[i+1][j] =4
        elif grid[i-1][j] ==x:
            grid[i-1][j] = 4
        elif grid[i][j+1] ==x:
            grid[i][j+1]= 4
        elif grid[i][j-1] ==x:
            grid[i][j-1] = 4
            
grid_fill() #temporally to avoid some bug when truck is created on top of black tile instead of road
for i in range(HEIGHT): #places truck on the left end of the first found horinzontal road
        if(grid[i][0]) == 1:
            grid[i][0] += 10
            break
j = 0


while IS_RUNNING:
    clock.tick(CLOCK_TICK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        
        if event.type == pygame.KEYDOWN:
            x=0
            y=0
            if event.key == pygame.K_UP: 
                x = -1
            elif event.key == pygame.K_LEFT:
                y = -1
            elif event.key == pygame.K_DOWN:
                x = 1
            elif event.key == pygame.K_RIGHT:
                y= 1
            elif event.key == pygame.K_r:
                randomize_trashes()
            elif event.key == pygame.K_SPACE:
                collect_trash(i,j)
            if x != 0 or y != 0:
                k = move(x,y,i,j)
                if k != False:
                    grid[i][j] -=10
                    i = k[0]
                    j = k[1]
                    grid[i][j] +=10
                    k = False
            


    render_window()


