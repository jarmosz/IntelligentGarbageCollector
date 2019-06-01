import map
import truck
from bfs import BreathFirstSearch
from random import randint, randrange


class DataParser:

    LEARNING_DATA_AMOUNT = 150
    SQUARE_SIZE = 5
    MAP_RESOLUTION = 15
    METHOD = "parse"

    def generate_learning_data(self):
        self.METHOD = "learning"
        counter = 0
        f = open("learning_data.txt", "w")
        while(counter < self.LEARNING_DATA_AMOUNT):
            move_list = []

            _map = map.Map(self.MAP_RESOLUTION)
            _map.generate_grid()
            _truck = truck.Truck(_map)
            _truck.set_current_map_state(_map.get_grid())
            _map.set_truck_current_position_on_the_grid(_truck)
            # Prepare trashes to visit
            for i in _map.grid:
                for j in i:
                    if j.get_type() == 'empty_trash' and randrange(0, 10) > 0:
                        j.type = "yellow_trash"

            move_list = BreathFirstSearch().start_bfs(_map, 'yellow_trash')
            decisions = len(move_list)

            move_list = [move for move in move_list if move != 'collect']

            decisions2 = len(move_list)

            previous_node = move_list[0]
            for i in range(1, len(move_list)):
                list = self.get_square(move_list[i], _map.get_grid())
                print("record saved")
                f.write(str(self.parse_move(previous_node,
                                            move_list[i])) + " " + str(list) + "\n")
                previous_node = move_list[i][:]
            counter += 1
            print("BFS-PRZED:", decisions)
            print("BFS-PO:", decisions2)
        print("Data generated successfully!")
        self.METHOD = 'parse'
        f.close()

    def convert_node_type(self, x, y, nodes):
        node_type = nodes[y][x].get_type()
        if(node_type == 'horizontal_straight_road' or node_type == 'vertical_straight_road' or node_type == 'cross_road'):
            return 2
        elif(node_type == 'grass'):
            return 1
        elif(node_type == 'empty_trash'):
            return 3
        elif(node_type == 'yellow_trash'):
            return 4

    def parse_move(self, previous, next):
        move = []
        if(previous[0] == next[0] and previous[1] > next[1]):
            move.append(5)
        elif(previous[0] == next[0] and previous[1] < next[1]):
            move.append(6)
        elif(previous[1] == next[1] and previous[0] > next[0]):
            move.append(7)
        elif(previous[1] == next[1] and previous[0] < next[0]):
            move.append(8)
        else:
            move.append(previous)
            move.append(next)

        return move

    def convert_small_grid(self, current_position, grid, first_range_start, first_range_end, second_range_start, second_range_end):
        square_list = []

        for i in range(first_range_start, first_range_end):
            for j in range(second_range_start, second_range_end):
                if i == current_position[1] and j == current_position[0]:
                    square_list.append(5)
                else:
                    square_list.append(
                        self.convert_node_type(j, i, grid))

        return square_list

    def update_grid(self, current_position, grid):
        trash_list = []
        x = current_position[0]
        y = current_position[1]
        type = 'yellow_trash'

        if x < len(grid[0])-1 and grid[y][x+1].get_type() == type:
            grid[y][x+1].type = 'empty_trash'
        if x > 0 and grid[y][x-1].get_type() == type and x:
            grid[y][x-1].type = 'empty_trash'
        if y < len(grid)-1 and grid[y+1][x].get_type() == type:
            grid[y+1][x].type = 'empty_trash'
        if y > 0 and grid[y-1][x].get_type() == type and y >= 0:
            grid[y-1][x].type = 'empty_trash'

    def get_square(self, current_position, grid):

        if(self.METHOD == 'learning'):
            self.update_grid(current_position, grid)

        if(current_position[0] == 0 or current_position[0] == 1):
            if current_position[1] == 0 or current_position[1] == 1:
                return self.convert_small_grid(current_position, grid, 0, self.SQUARE_SIZE, 0, self.SQUARE_SIZE)

            elif current_position[1] == self.MAP_RESOLUTION - 1 or current_position[1] == self.MAP_RESOLUTION - 2:
                return self.convert_small_grid(current_position, grid, self.MAP_RESOLUTION - self.SQUARE_SIZE, self.MAP_RESOLUTION, 0, self.SQUARE_SIZE)

            else:
                return self.convert_small_grid(current_position, grid, current_position[1] - 2, current_position[1] + 3, 0, self.SQUARE_SIZE)

        elif(current_position[0] == self.MAP_RESOLUTION - 1 or current_position[0] == self.MAP_RESOLUTION - 2):
            if current_position[1] == 0 or current_position[1] == 1:
                return self.convert_small_grid(current_position, grid, 0, self.SQUARE_SIZE, self.MAP_RESOLUTION - self.SQUARE_SIZE, self.MAP_RESOLUTION)

            elif current_position[1] == self.MAP_RESOLUTION - 1 or current_position[1] == self.MAP_RESOLUTION - 2:
                return self.convert_small_grid(current_position, grid, self.MAP_RESOLUTION - self.SQUARE_SIZE, self.MAP_RESOLUTION, self.MAP_RESOLUTION - self.SQUARE_SIZE, self.MAP_RESOLUTION)

            else:
                return self.convert_small_grid(current_position, grid, current_position[1] - 2, current_position[1] + 3, self.MAP_RESOLUTION - self.SQUARE_SIZE, self.MAP_RESOLUTION)

        elif(current_position[0] > 1 and current_position[0] < self.MAP_RESOLUTION - 2):
            if(current_position[1] == 0 or current_position[1] == 1):
                return self.convert_small_grid(current_position, grid, 0, self.SQUARE_SIZE, current_position[0] - 2, current_position[0] + 3)

            elif current_position[1] == self.MAP_RESOLUTION - 1 or current_position[1] == self.MAP_RESOLUTION - 2:
                return self.convert_small_grid(current_position, grid, self.MAP_RESOLUTION - self.SQUARE_SIZE, self.MAP_RESOLUTION, current_position[0] - 2, current_position[0] + 3)

            else:
                return self.convert_small_grid(current_position, grid, current_position[1] - 2, current_position[1] + 3, current_position[0] - 2, current_position[0] + 3)
