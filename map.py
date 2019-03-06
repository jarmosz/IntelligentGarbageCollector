import sys, pygame
from pygame.locals import *
from random import randint

WIDTH = 600
HEIGHT = 500
running = True
cellSize = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def gridUsingLines():
    for j in range(HEIGHT//cellSize+1): #+1 bo jak nie jest podzielne przez cellSize to na koncu sie nie rysuje
        pygame.draw.line(screen, BLACK, (0, j*cellSize), (WIDTH, j*cellSize), 1)
    for i in range(WIDTH//cellSize+1):
        pygame.draw.line(screen, BLACK, (i*cellSize, 0), (i*cellSize, HEIGHT), 1)

def gridUsingRectangles():
    for j in range(HEIGHT//cellSize):
        for i in range(WIDTH//cellSize):
            pygame.draw.rect(screen, BLACK, pygame.Rect(i*cellSize, j*cellSize, cellSize, cellSize), 1)

def renderWindow():
    screen.fill(WHITE)
    gridUsingRectangles()
    Path(5)
    pygame.display.update()

def Path(n): #generuje n punktow i laczy je linia
    points = []
    for i in range(n):
        points.append(tuple([randint(0, WIDTH), randint(0, HEIGHT)]))
    pygame.draw.lines(screen, GREEN, True, points, 2)

def colorRect(x, y, colour):
    pygame.draw.rect(screen, colour, pygame.Rect(x*cellSize, y*cellSize, cellSize, cellSize))

def drawBetweenPoints(x1, y1, x2, y2): #to wyznacza niby droge ale po chuju strasznie
    x = x1 #i tylko jesli x1<x2 i y1<y2 mozna to usunac
    y = y1
    colorRect(x, y, BLACK)
    while x != x2 or y != y2:
        a = randint(0,1)
        if a == 0 and x!=x2:
            x += 1
            colorRect(x, y, BLACK)
        elif a == 1 and y!=y2:
            y += 1
            colorRect(x, y, BLACK)
    #colorRect
        

def drawRoad(length, startingX, startingY): # to tez slabe 
    x = startingX
    y = startingY
    colored = []
    colorRect(x, y, BLACK)
    colored.append(tuple([x, y]))
    for i in range(length):
        direction = randint(1, 4) # 1 - up 2 - right 3 - down 4 - left
        if direction == 1 and y > 0:
            y -= 1
            colorRect(x, y, BLACK)
            colored.append(tuple([x, y]))
        elif direction == 2 and x < WIDTH // cellSize:
            x += 1
            colorRect(x, y, BLACK)
            colored.append(tuple([x, y]))
        elif direction == 3 and y < HEIGHT // cellSize:
            y += 1
            colorRect(x, y, BLACK)
            colored.append(tuple([x, y]))
        elif direction == 4 and x > 0:
            x -= 1
            colorRect(x, y, BLACK)
            colored.append(tuple([x, y]))
        else:
            i -= 1


while running:
    clock.tick(2)
    renderWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    
    