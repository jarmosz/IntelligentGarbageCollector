import sys
import pygame
from GridNode import GridNode
from random import randint
from RoadNode import RoadNode
from pygame.locals import *
from Vector2 import Vector2
WIDTH = 640
HEIGHT = 640
CELL_SIZE = 32
BLACK = (0, 0, 0)
GREEN = (77, 123, 77)
GRAY = (77, 77, 77)
WHITE = (255, 255, 255)
NUMBER_OF_ROWS = HEIGHT // CELL_SIZE
NUMBER_OF_COLUMNS = WIDTH // CELL_SIZE
MIN_RANDOMED_ROADS_VERTICALLY = 2
MAX_RANDOMED_ROADS_VERTICALLY = 4
MIN_RANDOMED_ROADS_HORIZONTALLY = 2
MAX_RANDOMED_ROADS_HORIZONTALLY = 4
roads = []  # graph with roads
randomized_points = []  # array with points in graph to walk through

grid = []
screen = pygame.display.set_mode((WIDTH, HEIGHT))
is_running = True
clock = pygame.time.Clock()


def initialize_list_grid():
    for i in range(0, NUMBER_OF_ROWS):
        m = []
        for j in range(0, NUMBER_OF_COLUMNS):
            m.append(i*j)
        grid.append(m)
        m = None


def generate_grid():
    for i in range(0, NUMBER_OF_ROWS):
        for j in range(0, NUMBER_OF_COLUMNS):
            current_node = GridNode()
            if i == 0:
                current_node.top_node = None
            else:
                current_node.top_node = grid[i-1][j]
                grid[i-1][j].bottom_node = current_node
            if j == 0:
                current_node.left_node = None
            else:
                current_node.left_node = grid[i][j-1]
                grid[i][j-1].right_node = current_node
            grid[i][j] = current_node
            del current_node
            grid[i][j].upper_node = None


def generate_roads():
    roads_vertically = randint(
        MIN_RANDOMED_ROADS_VERTICALLY, MAX_RANDOMED_ROADS_VERTICALLY)
    for i in range(0, roads_vertically):
        column = randint(1, NUMBER_OF_COLUMNS-2)
        if grid[0][column].upper_node != None or grid[0][column-1].upper_node != None or grid[0][column+1].upper_node != None:
            i = i-1
        else:
            for j in grid:
                current_node = RoadNode()
                if j[column].top_node == None:
                    pass
                else:
                    current_node.top_node = j[column].top_node.upper_node
                    j[column].top_node.upper_node.bottom_node = current_node
                current_node.position = Vector2(
                    column*CELL_SIZE, grid.index(j)*CELL_SIZE)
                j[column].upper_node = current_node
                roads.append(current_node)
                del current_node
    roads_horizontally = randint(
        MIN_RANDOMED_ROADS_HORIZONTALLY, MAX_RANDOMED_ROADS_HORIZONTALLY)
    for i in range(0, roads_horizontally):
        row = randint(1, NUMBER_OF_ROWS-2)
        if grid[row][0].upper_node != None or grid[row-1][0].upper_node != None or grid[row+1][0].upper_node != None:
            i = i-1
        else:
            for j in grid[row]:
                if j.left_node == None:
                    pass
                    current_node = RoadNode()
                else:
                    if j.upper_node == None:
                        current_node = RoadNode()
                    else:
                        current_node = j.upper_node
                    current_node.left_node = j.left_node.upper_node
                    j.left_node.upper_node.right_node = current_node
                j.upper_node = current_node
                current_node.position = Vector2(
                    grid[row].index(j)*CELL_SIZE, row*CELL_SIZE)
                roads.append(current_node)


def render_color(color, node):
    pygame.draw.rect(screen, color, pygame.Rect(
        node.position.x, node.position.y, CELL_SIZE, CELL_SIZE))


def render_screen_elements():

    for i in roads:
        # print(i.image)
        image = pygame.image.load(i.image)
        screen.blit(image, (i.position.x, i.position.y))
    for i in randomized_points:
        render_color(WHITE, i)


def render_window():
    screen.fill(GREEN)
    render_screen_elements()
    pygame.display.update()


def choose_road_sprites():
    for i in roads:
        i.choose_road_sprite()


def start():
    initialize_list_grid()
    generate_grid()
    generate_roads()
    randomize_points()
    choose_road_sprites()


def update():
    while is_running:
        clock.tick(2)
        render_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


def randomize_points():
    randomized_points.append(roads[2])
    randomized_points.append(roads[5])
    randomized_points.append(roads[-10])
    randomized_points.append(roads[-2])


start()
update()
