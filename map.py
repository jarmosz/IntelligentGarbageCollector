import sys
import os
import pygame
from pygame.locals import *
from random import randint
import random
import copy
import grass
import road
import trash
import truck
import numpy as np


class Map:
    CLOCK_TICK = 5
    CELL_SIZE = 32
    WIDTH = 15
    HEIGHT = 15
    RES_X = WIDTH * CELL_SIZE
    RES_Y = HEIGHT * CELL_SIZE
    MIN_ROADS_VERTICALLY = 2
    MAX_ROADS_VERTICALLY = 2
    MIN_ROADS_HORIZONTALLY = 2
    MAX_ROADS_HORIZONTALLY = 2
    NUMBER_OF_TRASH = 5

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k == "grid" or k == "truck":
                setattr(result, k, copy.deepcopy(v, memo))
        return result

    #def __deepcopy__(self, memo):
     #   return Map(copy.deepcopy(self.truck,self.grid, memo))

    def __init__(self, res):
        self.config_window_display(res)
        self.screen = pygame.display.set_mode((self.RES_X, self.RES_Y))
        self.clock = pygame.time.Clock()
        self.grid = [[0] * self.WIDTH for i in range(self.HEIGHT)]
        self.load_images()
        self.truck = None
        self.generate_grid()

    def config_window_display(self, res):
        self.RES_X = 32 * res
        self.RES_Y = 32 * res
        self.WIDTH = self.RES_X//self.CELL_SIZE
        self.HEIGHT = self.RES_Y//self.CELL_SIZE
        self.MIN_ROADS_VERTICALLY = res//5
        self.MAX_ROADS_VERTICALLY = res//3
        self.MIN_ROADS_HORIZONTALLY = res//5
        self.MAX_ROADS_HORIZONTALLY = res//3
        self.NUMBER_OF_TRASH = res//2

    def load_images(self):
        self.grass_image = pygame.image.load(grass.Grass.grass_path)
        self.trash_empty_image = pygame.image.load(
            trash.Trash.trash_empty_path)
        self.trash_yellow_image = pygame.image.load(
            trash.Trash.trash_yellow_path)
        self.trash_red_image = pygame.image.load(trash.Trash.trash_red_path)
        self.trash_blue_image = pygame.image.load(trash.Trash.trash_blue_path)
        self.road_horizontal_image = pygame.image.load(
            road.Road.road_horizontal_path)
        self.road_vertical_image = pygame.image.load(
            road.Road.road_vertical_path)
        self.road_crossroad_image = pygame.image.load(
            road.Road.road_crossroad_path)
        self.top_truck_image = pygame.image.load(truck.Truck.truck_top_path)
        self.down_truck_image = pygame.image.load(truck.Truck.truck_down_path)
        self.left_truck_image = pygame.image.load(truck.Truck.truck_left_path)
        self.right_truck_image = pygame.image.load(
            truck.Truck.truck_right_path)

    def import_map(self):
        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
            [0, 0, 0, 3, 1, 1, 1, 1, 1, 1, 1, 3, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [1, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 0, 3, 1, 1, 1, 1, 1, 1, 1, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.grid_refactoring()

    def generate_grid(self):

        roads_horizontally = randint(
            self.MIN_ROADS_HORIZONTALLY, self.MAX_ROADS_HORIZONTALLY)
        roads_vertically = randint(
            self.MIN_ROADS_VERTICALLY, self.MAX_ROADS_VERTICALLY)
        garbage_zone_vert = []
        garbage_zone_hor = []

        roads_horizontally = randint(
            self.MIN_ROADS_HORIZONTALLY, self.MAX_ROADS_HORIZONTALLY)
        roads_vertically = randint(
            self.MIN_ROADS_VERTICALLY, self.MAX_ROADS_VERTICALLY)
        garbage_zone_ver = []
        garbage_zone_hor = []
        i = 0
        print('roads x: ' + str(roads_horizontally))
        print('roads y: ' + str(roads_vertically))
        while i < roads_horizontally:
            y = randint(1, self.HEIGHT - 2)
            if(self.grid[y][0] == 0 and self.grid[y - 1][0] == 0 and self.grid[y + 1][0] == 0):
                for x in range(self.WIDTH):
                    self.grid[y][x] += 1
                garbage_zone_hor += [y + 1, y - 1]
                i += 1
        i = 0
        while i < roads_vertically:
            x = randint(1, self.WIDTH - 2)
            if(self.grid[0][x] == 0 and self.grid[0][x - 1] == 0 and self.grid[0][x + 1] == 0):
                for j in self.grid:
                    j[x] += 2
                garbage_zone_ver += [x + 1, x - 1]
                i += 1
        garbage_zone_hor = list(set(garbage_zone_hor))
        garbage_zone_ver = list(set(garbage_zone_ver))
        garbage_zone = []
        for i in garbage_zone_hor:
            for j in range(0, self.WIDTH):
                if self.grid[i][j] == 0:
                    garbage_zone.append((i, j))
        for i in garbage_zone_ver:
            for j in range(0, self.HEIGHT):
                if self.grid[j][i] == 0:
                    garbage_zone.append((j, i))
        garbage_zone = list(set(garbage_zone))
        bins = random.choices(garbage_zone, k=self.NUMBER_OF_TRASH)
        for i in range(self.NUMBER_OF_TRASH):
            x, y = bins[i]
            self.grid[x][y] = 4
        self.grid_refactoring()

    def if_all_trashes_visited(self):
        visited = True
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                self.grid[i][j].get_type() == "yellow_trash"
                visited = False
                break

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
        self.fill_with_trash(1)

    def get_grid(self):
        return self.grid

    def get_grid_cell(self, x, y):
        return self.grid[x][y]

    def set_grid_cell(self, x, y, new_object):
        self.grid[x][y] = new_object

    def fill_with_trash(self, prob):
        for i in self.grid:
            for j in i:
                if j.get_type() == 'empty_trash' and random.random() < prob:
                    j.type = "yellow_trash"

    def get_grid_numerical(self):
        grid = np.array(self.grid)
        numerical_grid = np.array([self.type_as_num(row) for row in grid])
        numerical_grid = np.pad(numerical_grid, pad_width=2, mode='constant')
        return numerical_grid

    def type_as_num(self, objects):
        types_nums = {"grass": 0,
                      'horizontal_straight_road': 1,
                      'vertical_straight_road': 1,
                      'cross_road': 1,
                      'empty_trash': 2,
                      'yellow_trash': 3}
        return [types_nums[obj.type] for obj in objects]

    def set_truck_current_position_on_the_grid(self, truck):
        self.truck = truck

    def render_window(self):
        self.clock.tick(self.CLOCK_TICK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def chose_image_to_display(self, type):
        if type == 'grass':
            return self.grass_image
        elif type == 'horizontal_straight_road':
            return self.road_horizontal_image
        elif type == 'vertical_straight_road':
            return self.road_vertical_image
        elif type == 'cross_road':
            return self.road_crossroad_image
        elif type == 'empty_trash':
            return self.trash_empty_image
        elif type == 'yellow_trash':
            return self.trash_yellow_image
        elif type == 'blue_trash':
            return self.trash.trash_blue_image
        elif type == 'red_trash':
            return self.trash_red_image
        elif type == 'truck_left':
            return self.left_truck_image
        elif type == 'truck_right':
            return self.right_truck_image
        elif type == 'truck_down':
            return self.down_truck_image
        elif type == 'truck_top':
            return self.top_truck_image
        else:
            print("error during chosing images")

    def render_map(self):

        for idx, i in enumerate(self.grid):
            for jdx, j in enumerate(i):
                self.screen.blit(self.chose_image_to_display(
                    j.get_type()), (jdx*self.CELL_SIZE, idx*self.CELL_SIZE))
        self.screen.blit(self.chose_image_to_display(self.truck.get_type()), (self.truck.get_current_position_x(
        )*self.CELL_SIZE, self.truck.get_current_position_y()*self.CELL_SIZE))

    def update_window(self):
        self.render_map()
        pygame.display.update()
