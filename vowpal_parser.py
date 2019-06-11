import map
import truck
from bfs import BreathFirstSearch
from itertools import groupby

# 0-grass 1-road 2-trash empty 3-trash full
#5-collect 6-up 7-down 8-left 9-right
class VowpalParser:
    SQUARE_SIZE = 7
    MAP_RESOLUTION = 10
    NUMBER_OF_MAPS = 1
    PAD = int(SQUARE_SIZE//2)

    def collect_data(self):
        file = open("vowpal_data.txt", "w")
        for j in range(self.NUMBER_OF_MAPS):
            _map = map.Map(self.MAP_RESOLUTION)
            _truck = truck.Truck(_map)
            _truck.set_current_map_state(_map.get_grid())
            _map.set_truck_current_position_on_the_grid(_truck)
            map_numerical = _map.get_grid_numerical(self.PAD)
            move_list = [(_truck.current_position_x,
                          _truck.current_position_y)]
            move_list += BreathFirstSearch().start_bfs(_map, 'yellow_trash')
            prev = move_list[0]
            for i in range(1, len(move_list)):
                state = ' '
                index = 0
                if move_list[i] == 'collect':
                    square_state = self.get_grid_square(map_numerical, prev)
                    move = 5
                else:
                    square_state = self.get_grid_square(map_numerical, prev)
                    move = str(self.parse_move(prev, move_list[i]))
                    prev = move_list[i]
                for rows in square_state:
                    for value in rows:
                        state += ''.join('f{}:{} '.format(index, value))
                        index += 1
                #print(square_state)
                file.write("{} | {}\n".format(str(move), state))
                square_state = self.empty_trash(square_state)
            file.close()

    def parse_move(self, previous, next):
        if(previous[0] == next[0] and previous[1] > next[1]):
            return 6
        elif(previous[0] == next[0] and previous[1] < next[1]):
            return 7
        elif(previous[1] == next[1] and previous[0] > next[0]):
            return 8
        return 9

    def get_grid_square(self, grid, current_position):
        # adjusting current position to correct one
        x = current_position[0] + self.PAD
        y = current_position[1] + self.PAD  # after numpy.pad
        square = grid[y-self.PAD:y+self.PAD+1,
                     x-self.PAD:x+self.PAD+1]
        return square

    def empty_trash(self, grid):
        print(grid)
        pos = self.PAD
        if grid[pos-1, pos] == 3:
            grid[pos-1, pos] = 2
            return grid
        elif grid[pos, pos-1] == 3:
            grid[pos, pos-1] = 2
            return grid
        elif grid[pos+1, pos] == 3:
            grid[pos+1, pos] = 2
            return grid
        elif grid[pos, pos+1] == 3:
            grid[pos, pos+1] = 2
            return grid
