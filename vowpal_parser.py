import map
import truck
from bfs import BreathFirstSearch
from itertools import groupby

# 0 - grass 1 - road 2 - trash empty 3 - trash full


class VowpalParser:
    SQUARE_SIZE = 5
    MAP_RESOLUTION = 10
    NUMBER_OF_MAPS = 1

    def collect_data(self):
        f = open("vowpal_data.txt", "w")
        for j in range(self.NUMBER_OF_MAPS):
            _map = map.Map(self.MAP_RESOLUTION)
            _truck = truck.Truck(_map)
            _truck.set_current_map_state(_map.get_grid())
            _map.set_truck_current_position_on_the_grid(_truck)
            map_numerical = _map.get_grid_numerical()
            move_list = [(_truck.current_position_x,
                          _truck.current_position_y)]
            move_list += BreathFirstSearch().start_bfs(_map, 'yellow_trash')
            prev = move_list[0]
            print(move_list)
            print(map_numerical)
            #for i in move_list[2:]:
            #    if i == 'collect'
            for i in range(1, len(move_list)):
                if move_list[i] == 'collect':
                    square_state = self.get_grid_square(map_numerical, prev)
                    move = 'c'
                    state = ' '.join(' '.join(str(x) for x in row)
                                     for row in square_state)
                else:
                    square_state = self.get_grid_square(map_numerical, prev)
                    move = str(self.parse_move(prev, move_list[i]))
                    prev = move_list[i]
                #print('{}\n{}'.format(move, square_state))
                state = ' '.join(' '.join(str(x) for x in row)
                                 for row in square_state)
                f.write("{}|{}\n".format(str(move), state))
                square_state = self.empty_trash(square_state)
            f.close()
        while(True):
            _map.update_window()
            _map.render_window()

    def parse_move(self, previous, next):
        if(previous[0] == next[0] and previous[1] > next[1]):
            return "u"
        elif(previous[0] == next[0] and previous[1] < next[1]):
            return "d"
        elif(previous[1] == next[1] and previous[0] > next[0]):
            return "l"
        return "r"

    def get_grid_square(self, grid, current_position):
        # adjusting current position to corrent one
        x = current_position[0] + self.SQUARE_SIZE//2
        y = current_position[1] + self.SQUARE_SIZE//2  # after numpy.pad
        square = grid[y-2:y+3, x-2:x+3]
        return square

    def empty_trash(self, grid):
        if grid[1, 2] == 3:
            grid[1, 2] = 2
            return grid
        elif grid[2, 1] == 3:
            grid[2, 1] = 2
            return grid
        elif grid[3, 2] == 3:
            grid[3, 2] = 2
            return grid
        elif grid[2, 3] == 3:
            grid[2, 3] = 2
            return grid
