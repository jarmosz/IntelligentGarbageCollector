from random import choice
import map
import truck
import copy
from moves import Move
import sys
import decision_tree
import data_parser
type_of_trash = None
s = 0
move_list = []
sys.setrecursionlimit(12000)


class VisualizeDT:

    def start_vdt(self, _map, _type_of_trash):
        global type_of_trash
        global _data_parser
        global _decision_tree
        _data_parser = data_parser.DataParser()
        _data_parser.generate_learning_data()
        type_of_trash = _type_of_trash
        _decision_tree = decision_tree.DecisionTree()
        _decision_tree.learn_tree()
        self.create_tree(move_list, _map,  0)
        return move_list

    def create_tree(self, current_move_list, current_grid,  recursion_depth):

        global s
        print(s)
        recursion_depth += 1
        if recursion_depth > 11000:
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
                self.create_tree(new_move_lits, new_grid,
                                 recursion_depth)
        else:
            current_position = (current_grid.truck.get_current_position_x(
            ), current_grid.truck.get_current_position_y())
            data_square = _data_parser.get_square(
                current_position, current_grid.get_grid())
            possible_move = _decision_tree.predict_result(data_square)
            possible_move = self.parse_move(possible_move)
            print("Learned:", possible_move)

            truck_position = (current_grid.truck.get_current_position_x(
            ), current_grid.truck.get_current_position_y())
            while(not self.can_move_to(current_grid, truck_position, possible_move)):
                move_choice = [Move.MOVE_TOP, Move.MOVE_DOWN,
                               Move.MOVE_RIGHT, Move.MOVE_LEFT]
                possible_move = choice(move_choice)

            print("Gen: ", possible_move)
            new_grid = copy.deepcopy(current_grid)
            new_move_list = copy.deepcopy(current_move_list)
            new_grid.truck.make_move(possible_move)
            new_move_list.append(possible_move)
            self.create_tree(new_move_list, new_grid, recursion_depth)
        return

    def check_if_is_done(self, m):
        for i in m.grid:
            for j in i:
                if j.get_type() == type_of_trash:
                    return False
        return True

    def can_move_to(self, current_grid, current_position, move):
        tem_x = 0
        tem_y = 0
        if(move == Move.MOVE_TOP):
            tem_x = current_grid.truck.get_current_position_x()
            tem_y = current_grid.truck.get_current_position_y() - 1
        elif(move == Move.MOVE_DOWN):
            tem_x = current_grid.truck.get_current_position_x()
            tem_y = current_grid.truck.get_current_position_y() + 1
        elif(move == Move.MOVE_LEFT):
            tem_x = current_grid.truck.get_current_position_x() - 1
            tem_y = current_grid.truck.get_current_position_y()
        elif(move == Move.MOVE_RIGHT):
            tem_x = current_grid.truck.get_current_position_x() + 1
            tem_y = current_grid.truck.get_current_position_y()

        return current_grid.truck.can_move_to(tem_x, tem_y)

    def parse_move(self, move):
        possible_move = []
        if move[0] == 5:
            possible_move.append(Move.MOVE_TOP)
        elif move[0] == 6:
            possible_move.append(Move.MOVE_DOWN)
        elif move[0] == 7:
            possible_move.append(Move.MOVE_LEFT)
        elif move[0] == 8:
            possible_move.append(Move.MOVE_RIGHT)

        return possible_move

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
