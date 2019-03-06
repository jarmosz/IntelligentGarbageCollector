import sys, pygame

from pygame.locals import *

WIDTH = 600
HEIGHT = 500
running = True
cellSize = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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
    pygame.display.update()

while running:
    clock.tick(2)
    renderWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    
    