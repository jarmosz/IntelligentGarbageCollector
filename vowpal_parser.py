import map
import truck
import numpy as np
from bfs import BreathFirstSearch
from random import randrange


class VowpalParser:
    SQUARE_SIZE = 5
    MAP_RESOLUTION = 40

    def collect_data(self):
        f = open("vowpal_data.txt", "w")
        move_list = []
        _map = map.Map(6)
        _map.generate_grid()
        _truck = truck.Truck(_map)
        _truck.set_current_map_state(_map.get_grid())
        _map.set_truck_current_position_on_the_grid(_truck)
        for i in _map.grid:
            for j in i:
                if j.get_type() == 'empty_trash' and randrange(0, 10) > 6:
                    j.type = "yellow_trash"

        move_list.append((_truck.current_position_x, _truck.current_position_y))
        move_list += BreathFirstSearch().start_bfs(_map, 'yellow_trash')
        move_list = [move for move in move_list if move != 'collect']
        print(move_list)
        prev = move_list[0]
        for i in range(1, len(move_list)):
            square_state = self.get_grid_square(_map.get_grid_numerical(), move_list[i])
            state = ' '.join(' '.join(str(x) for x in row) for row in square_state)
            move = str(self.parse_move(prev, move_list[i]))
            f.write("{}|{}\n".format(str(move), state))
            prev = move_list[i][:]
        f.close()
        while(True):
            _map.update_window()
            _map.render_window()
    
    def parse_move(self, previous, next):
        move = []
        if(previous[0] == next[0] and previous[1] > next[1]):
            return "u"
        elif(previous[0] == next[0] and previous[1] < next[1]):
            return "d"
        elif(previous[1] == next[1] and previous[0] > next[0]):
            return "l"
        elif(previous[1] == next[1] and previous[0] < next[0]):
            return "r"
    
    def get_grid_square(self, grid, current_position):
        x = current_position[0] + 2
        y = current_position[1] + 2
        square = grid[y-2:y+3, x-2:x+3]
        square[2,2] = 5
        return square
        

        
        






