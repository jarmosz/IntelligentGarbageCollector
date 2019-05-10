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

    def start_a_star(self, _map, _type_of_trash):
        global type_of_trash
        type_of_trash = _type_of_trash
        # as we start, we need to know which trash we want to visit first
        nearest_trash = _map.truck.find_next_trash_to_visit(type_of_trash)[:]
        self.create_tree(move_list, _map, nearest_trash, 0)
        return move_list

    def create_tree(self, current_move_list, current_grid, nearest_trash, recursion_depth):
        global s
        print(s)
        recursion_depth += 1
        if recursion_depth > 1300:
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

        if self.check_if_is_done(current_grid):
            if move_list == [] or len(move_list) > len(current_move_list):
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
                for trash in trash_around:
                    if(trash == current_grid[(nearest_trash[1])][(nearest_trash[0])]):
                        nearest_trash = new_grid.truck.find_next_trash_to_visit(type_of_trash)[
                            :]
                self.create_tree(new_move_lits, new_grid,
                                 nearest_trash, recursion_depth)
        else:
            possible_moves = current_grid.truck.generate_possible_moves_to_achieve_nearest_trash(
                nearest_trash)
            if possible_moves == []:
                return
            for i in possible_moves:
                if not i == last_move:
                    new_grid = copy.deepcopy(current_grid)
                    new_move_list = copy.deepcopy(current_move_list)
                    new_grid.truck.make_move(i)
                    new_move_list.append(i)
                    self.create_tree(new_move_list, new_grid,
                                     nearest_trash, recursion_depth)
        return

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
