import sys
import os
import pygame
from pygame.locals import * 
from random import randint
import random

import grass
import road
import trash
import truck

class Map:

    CLOCK_TICK = 30
    RES_X = 1280
    RES_Y = 640
    CELL_SIZE = 32
    WIDTH = RES_X//CELL_SIZE
    HEIGHT = RES_Y//CELL_SIZE
    MIN_ROADS_VERTICALLY = 4
    MAX_ROADS_VERTICALLY = 6
    MIN_ROADS_HORIZONTALLY = 4
    MAX_ROADS_HORIZONTALLY = 6


    def __init__(self):
        self.screen = pygame.display.set_mode((self.RES_X, self.RES_Y))
        self.clock = pygame.time.Clock()
        self.grid = [[0] * self.WIDTH for i in range(self.HEIGHT)]


    def generate_grid(self):

        roads_horizontally = randint(self.MIN_ROADS_HORIZONTALLY, self.MAX_ROADS_HORIZONTALLY)
        roads_vertically = randint(self.MIN_ROADS_VERTICALLY, self.MAX_ROADS_VERTICALLY)
        garbage_zone_vert = []
        garbage_zone_hor = []

        roads_horizontally = randint(self.MIN_ROADS_HORIZONTALLY, self.MAX_ROADS_HORIZONTALLY)
        roads_vertically = randint(self.MIN_ROADS_VERTICALLY, self.MAX_ROADS_VERTICALLY)
        garbage_zone_vert = []
        garbage_zone_hor = []
        i = 0
        print('roads x: ' + str(roads_horizontally))
        print('roads y: ' + str(roads_vertically))
        while i < roads_horizontally:
            y = randint(1, self.HEIGHT - 2)    
            if(self.grid[y][0] == 0 and self.grid[y - 1][0] == 0 and self.grid[y + 1][0] == 0):
                for x in range(self.WIDTH):
                    self.grid[y][x] += 1
                garbage_zone_vert += [y + 1, y - 1]
                i += 1
        i = 0
        while i < roads_vertically:  
            x = randint(1, self.WIDTH - 2) 
            if(self.grid[0][x] == 0 and self.grid[0][x - 1] == 0 and self.grid[0][x + 1] == 0):
                for j in self.grid:
                    j[x] += 2
                garbage_zone_hor += [x + 1, x - 1]
                i += 1
    
        for i in range(randint(6, 20)):
            rand_vert = random.choice(garbage_zone_vert)
            rand_trashcan_vert = randint(0, self.WIDTH - 1)
            rand_hor = random.choice(garbage_zone_hor)
            rand_trashcan_hor = randint(0, self.HEIGHT - 1)

            if(self.grid[rand_vert][rand_trashcan_vert]) == 0:
                self.grid[rand_vert][rand_trashcan_vert] = 4
            if(self.grid[rand_trashcan_hor][rand_hor]) == 0:
                self.grid[rand_trashcan_hor][rand_hor] = 4

        self.grid_refactoring()
    

    def grid_refactoring(self):
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if(self.grid[i][j] == 0):
                    self.grid[i][j] = grass.Grass()
                elif(self.grid[i][j] == 1):
                    self.grid[i][j] = road.Road("horizontal_straight_road")
                elif(self.grid[i][j] == 2):
                    self.grid[i][j] = road.Road("vertical_straight_road")
                elif(self.grid[i][j] == 3):
                    self.grid[i][j] = road.Road("cross_road")
                elif(self.grid[i][j] == 4):
                    self.grid[i][j] = trash.Trash("empty_trash")
                elif(self.grid[i][j] == 5):
                    self.grid[i][j] = trash.Trash("yellow_trash")
                elif(self.grid[i][j] == 6):
                    self.grid[i][j] = trash.Trash("blue_trash")
                elif (self.grid[i][j] == 7):
                    self.grid[i][j] = trash.Trash("red_trash")

    
    def get_grid(self):
        return self.grid

    def get_grid_cell(self, x , y):
        return self.grid[x][y]

    def set_grid_cell(self, x, y, new_object):
        self.grid[x][y] = new_object


    def get_truck_current_position_on_the_grid(self, truck):
        self.truck = truck

    def render_window(self):
        self.clock.tick(self.CLOCK_TICK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def render_map(self):
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if i == self.truck.get_current_position_y() and j == self.truck.get_current_position_x():
                    self.screen.blit(pygame.image.load(self.grid[i][j].get_texture()), (j*self.CELL_SIZE, i*self.CELL_SIZE))
                    self.screen.blit(pygame.image.load(self.truck.get_texture()), (j*self.CELL_SIZE, i*self.CELL_SIZE))
                    self.truck.get_current_position_x()
                    self.truck.get_current_position_y()
                else:
                    self.screen.blit(pygame.image.load(self.grid[i][j].get_texture()), (j*self.CELL_SIZE, i*self.CELL_SIZE))   


    def update_window(self):
        self.render_map()
        pygame.display.update()

    

