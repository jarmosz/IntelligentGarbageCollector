import map
import truck
import copy
from moves import Move
import sys
type_of_trash = None
move_list = []
s = 0
sys.setrecursionlimit(12000)


class BestFirstSearch:

    def start_A_star(self, _map, _type_of_trash):
        global type_of_trash
        global starter_x
        global starter_y
        global visited_nodes
        visited_nodes = []
        type_of_trash = _type_of_trash
        nearest_trash = _map.truck.find_next_trash_to_visit(type_of_trash)
        pom = []
        starter_x = _map.truck.get_current_position_x()
        starter_y = _map.truck.get_current_position_y()
        pom.append(starter_x)
        pom.append(starter_y)
        visited_nodes.append(pom)
        self.create_tree(move_list, _map, nearest_trash,  0)
        return move_list

    def create_tree(self, current_move_list, current_grid, nearest_trash, recursion_depth):
        global s
        print(s)
        recursion_depth += 1
        if recursion_depth > 10000:
            return
        global type_of_trash
        global move_list

        s = s+1
        print(s)
        if current_move_list != []:
            last_move = current_move_list[-1]
        else:
            last_move = ''
        last_move = self.reverse_move(last_move)

        if(nearest_trash == []):
            move_list = current_move_list
            return
            

        trash_around = current_grid.truck.find_trash_around(
            type_of_trash)  # returns list with trash of certain kind
        if trash_around != []:
            for i in trash_around:
                new_grid = copy.deepcopy(current_grid)
                new_move_lits = copy.deepcopy(current_move_list)
                new_move_lits.append('collect')
                tmp = new_grid.truck.find_trash_around(type_of_trash)
                trash_to_collect_on_new_grid = tmp[0]
                new_grid.truck.collect_trash(trash_to_collect_on_new_grid)
            
            nearest_trash = new_grid.truck.find_next_trash_to_visit(type_of_trash)
            self.create_tree(new_move_lits, new_grid, nearest_trash, recursion_depth)
        else:
            print("zmierzam do:", nearest_trash)

            recent_move = "right"

            if(current_move_list != []):
                if current_move_list[-1] == Move.MOVE_LEFT:
                    recent_move = "left"
                elif current_move_list[-1] == Move.MOVE_RIGHT:
                    recent_move = "right"
                elif current_move_list[-1] == Move.MOVE_TOP:
                    recent_move = "top"
                elif current_move_list[-1] == Move.MOVE_DOWN:
                    recent_move = "bottom"
            else:
                recent_move = "left"

            possible_moves = current_grid.truck.get_next_move(nearest_trash, starter_x, starter_y, current_grid, recent_move)
  
            new_grid = copy.deepcopy(current_grid)
            new_move_list = copy.deepcopy(current_move_list)
            for i in possible_moves:
                new_grid = copy.deepcopy(current_grid)
                new_move_list = copy.deepcopy(current_move_list)
                new_grid.truck.make_move(i)
                current_truck_position = []
                current_truck_position.append(new_grid.truck.get_current_position_x())
                current_truck_position.append(new_grid.truck.get_current_position_y())
                visited_nodes.append(current_truck_position)
                new_move_list.append(i)
                self.create_tree(new_move_list, new_grid, nearest_trash, recursion_depth)
        

    def check_if_is_done(self, m):
        for i in m.grid:
            for j in i:
                if j.get_type() == type_of_trash:
                    return False
        return True

    def reverse_move(self, move):
        last_move = ''
        if move == Move.MOVE_LEFT:
            last_move = Move.MOVE_RIGHT
        elif move == Move.MOVE_RIGHT:
            last_move = Move.MOVE_LEFT
        elif move == Move.MOVE_TOP:
            last_move = Move.MOVE_DOWN
        elif move == Move.MOVE_DOWN:
            last_move = Move.MOVE_TOP
        return last_move
