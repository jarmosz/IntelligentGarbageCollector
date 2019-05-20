import map
import truck
import copy
from moves import Move
import sys
import queue
from collections import deque
type_of_trash = None
move_list = []
s = 0
q = deque([((), [])])
# q = queue.Queue()
move_list = []
trashes = []


class BreathFirstSearch:

    def start_bfs(self, _map,  _type_of_trash):
        global type_of_trash
        global q
        type_of_trash = _type_of_trash
        starting_pos = ((_map.truck.get_current_position_x(),
                        _map.truck.get_current_position_y()))
        q = deque([(starting_pos, [])])
        print("qstart: ", q)
        self.find_path_bfs(_map, move_list, q)
        return move_list

    def find_path_bfs(self, grid, current_move_list, q):
        goal = (8, 8)
        global move_list
        # current_q = deque([(start, [])])
        if self.check_if_is_done(grid):
            if move_list == [] or len(move_list) > len(current_move_list):
                print("siemankoo")
                move_list = current_move_list
                #current_move_list.clear()
            return
        trash_around = grid.truck.find_trash_around(type_of_trash)
        if trash_around != []:
            for i in trash_around:
                new_grid = copy.deepcopy(grid)
                new_move_list = copy.deepcopy(current_move_list)
                new_move_list.append("collect")
                tmp = new_grid.truck.find_trash_around(type_of_trash)
                trash_to_collect = tmp[0]
                new_grid.truck.collect_trash(trash_to_collect)               
                self.find_path_bfs(new_grid, new_move_list, q)
        else:
            curr, path = q.popleft()
            print("truck pos: ", curr)
            print("path: ", path)
            new_grid = copy.deepcopy(grid)
            new_grid.truck.move_to(curr[0], curr[1])
            new_move_list = copy.deepcopy(current_move_list)
            new_move_list.append((curr[0], curr[1]))  
            possible_cord = new_grid.truck.possible_cord()
            print("possible:", possible_cord)
            if possible_cord == []:
                return
            for i in possible_cord:
                if i not in current_move_list and i[0] != 0:
                    print("move:", i)
                    print("visited:", current_move_list)
                    # q.append((i, path + [curr]))
                    #visited.add(i)
                                             # new_q.append((i, path + [i]))
                    q.append((i, path + [curr]))             
                    print("q after app:", q)
            '''if not q:
                move_list = path[:] + [curr]'''
            self.find_path_bfs(new_grid, new_move_list, q)


        '''trash_around = grid.truck.find_trash_around(type_of_trash)
            if trash_around != []:
                for i in trash_around:
                    move_list.append('collect')
                    tmp = grid.truck.find_trash_around(type_of_trash)
                    trash_to_collect_on_new_grid = tmp[0]
                    grid.truck.collect_trash(trash_to_collect_on_new_grid)
                    
            else:
                possible_moves = grid.truck.possible_moves()
                if possible_moves == []:
                    return
                for i in possible_moves:
                    if not i == last_move and i not in visited:
                        q.put(i)'''
                       
    
    def check_if_is_done(self, m):
        for i in m.grid:
            for j in i:
                if j.get_type() == type_of_trash:
                    return False
        return True
