import map
from bfs import BreathFirstSearch
class VowpalParser:
    SQUARE_SIZE = 5
    MAP_RESOLUTION = 6

    def collect_data(self):
        f = open("vowpal_data.txt", "w")
        _map = map.Map(self.MAP_RESOLUTION)
        move_list = BreathFirstSearch().start_bfs(_map, 'yellow_trash')
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
        if(previous[0] == next[0] and previous[1] > next[1]):
            return "u"
        elif(previous[0] == next[0] and previous[1] < next[1]):
            return "d"
        elif(previous[1] == next[1] and previous[0] > next[0]):
            return "l"
        return "r"
    
    def get_grid_square(self, grid, current_position):
        x = current_position[0] + self.SQUARE_SIZE//2 #adjusting current position to corrent one
        y = current_position[1] + self.SQUARE_SIZE//2 #after numpy.pad
        square = grid[y-2:y+3, x-2:x+3]
        square[2,2] = 5 #truck in the middle
        return square
    
    
        

        
        






