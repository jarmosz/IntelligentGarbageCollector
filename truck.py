import map
import os
import math
from moves import Move


class Truck:

    folder = os.path.dirname(os.path.realpath(
        __file__))  # get project's folder
    truck_right_path = os.path.join(folder, 'sprites/truck_right.png')
    truck_left_path = os.path.join(folder, 'sprites/truck_left.png')
    truck_top_path = os.path.join(folder, 'sprites/truck_top.png')
    truck_down_path = os.path.join(folder, 'sprites/truck_down.png')

    def __init__(self, map):
        self.type = "truck_right"
        self.current_position_x = 0
        self.current_position_y = 0
        self.grid = map.grid
        self.set_starting_position_on_the_grid()
        self.offset_x = 0
        self.offset_y = 0

    def set_current_position_x(self, new_position_x):
        self.current_position_x = new_position_x

    def set_current_position_y(self, new_position_y):
        self.current_position_y = new_position_y

    def get_current_position_x(self):
        return self.current_position_x

    def get_current_position_y(self):
        return self.current_position_y

    def set_current_map_state(self, current_grid):
        self.grid = current_grid

    def set_starting_position_on_the_grid(self):
        for y in range(len(self.grid)):
            if self.grid[y][0].get_type() == "horizontal_straight_road":
                self.current_position_x = 0
                self.current_position_y = y
                break

    def get_type(self):
        return self.type

    def can_move_to(self, x, y):
        if x < len(self.grid[0]) and y < len(self.grid) and x >= 0 and y >= 0:
            if (self.grid[y][x].get_type() == "horizontal_straight_road") or (self.grid[y][x].get_type() == "vertical_straight_road") or (self.grid[y][x].get_type() == "cross_road"):
                return True
        return False

    def find_trash_around(self, type):
        trash_list = []
        x = self.current_position_x
        y = self.current_position_y

        if x < len(self.grid[0])-1 and self.grid[y][x+1].get_type() == type:
            trash_list.append(self.grid[y][x+1])
        if x > 0 and self.grid[y][x-1].get_type() == type and x:
            trash_list.append(self.grid[y][x-1])
        if y < len(self.grid)-1 and self.grid[y+1][x].get_type() == type:
            trash_list.append(self.grid[y+1][x])
        if y > 0 and self.grid[y-1][x].get_type() == type and y >= 0:
            trash_list.append(self.grid[y-1][x])

        return trash_list

    def find_trash(self, type, x, y):
        trash_list=[]
        if x< len(self.grid[0])-1 and self.grid[y][x+1].get_type() == type  :
            trash_list.append(self.grid[y][x+1])
        if x> 0 and self.grid[y][x-1].get_type() == type and x:
            trash_list.append(self.grid[y][x-1])
        if y <len(self.grid)-1 and self.grid[y+1][x].get_type() == type:
            trash_list.append(self.grid[y+1][x])
        if y>0 and self.grid[y-1][x].get_type() == type and y >=0 :
            trash_list.append(self.grid[y-1][x])

        return trash_list

    # Functions for A*

    # Count Heuristic via Manhattan format

    def count_heuristic_from_a_to_b(self, current_x, current_y, goal_x, goal_y):
        return abs(goal_x - current_x) + abs(goal_y - current_y)

    # Find nearest trash to visit using Heuristic function

    def find_next_trash_to_visit(self, type):
        not_visited_trashes = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j].get_type() == type:
                    pom_list = []
                    pom_list.append(j)
                    pom_list.append(i)
                    not_visited_trashes.append(pom_list)

        x = self.get_current_position_x()
        y = self.get_current_position_y()
        measure = 100.0
        nearest_trash = []
        for trash in not_visited_trashes:
            next_measure = self.count_heuristic_from_a_to_b(
                x, y, trash[0], trash[1])
            if(next_measure < measure):
                measure = next_measure
                nearest_trash = trash[:]

        return nearest_trash

    def count_route_wage_vertically_top(self, x, y, _map):
        counter = 0
        for i in range(0, y+1):
            for j in range(x, x+1):
                if(_map.get_grid()[i][j].get_type() == "horizontal_straight_road" or _map.get_grid()[i][j].get_type() == "vertical_straight_road" or _map.get_grid()[i][j].get_type() == "cross_road"):
                    counter = counter + 1
        return counter

    def count_route_wage_vertically_down(self, x, y, _map):
        counter = 0
        for i in range(y, 6):
            for j in range(x, x+1):
                if(_map.get_grid()[i][j].get_type() == "horizontal_straight_road" or _map.get_grid()[i][j].get_type() == "vertical_straight_road" or _map.get_grid()[i][j].get_type() == "cross_road"):
                    counter = counter + 1
        return counter

    def count_route_wage_horizontally_right(self, x, y, _map):
        counter2 = 0
        for i in range(y, len(_map.get_grid())):
            for j in range(x, 6):
                if(_map.get_grid()[i][j].get_type() == "horizontal_straight_road" or _map.get_grid()[i][j].get_type() == "vertical_straight_road" or _map.get_grid()[i][j].get_type() == "cross_road"):
                    counter2 = counter2 + 1
        return counter2

    def count_route_wage_horizontally_left(self, x, y, _map):
        counter2 = 0
        for i in range(y, len(_map.get_grid())):
            for j in range(0, x+1):
                if(_map.get_grid()[i][j].get_type() == "horizontal_straight_road" or _map.get_grid()[i][j].get_type() == "vertical_straight_road" or _map.get_grid()[i][j].get_type() == "cross_road"):
                    counter2 = counter2 + 1
        return counter2

    def get_next_move(self, nearest_trash, starter_x, starter_y, current_grid, recent_move):

        possible_moves = []

        x = self.get_current_position_x()
        y = self.get_current_position_y()

        if(self.can_move_down()):
            bottom = self.count_heuristic_from_a_to_b(x, y+1, nearest_trash[0], nearest_trash[1])
        else:
            bottom = 8000

        if(self.can_move_left()):
             left = self.count_heuristic_from_a_to_b(x-1, y, nearest_trash[0], nearest_trash[1])
        else:
            left = 8000

        if(self.can_move_top()):
            top = self.count_heuristic_from_a_to_b(x, y-1, nearest_trash[0], nearest_trash[1])
        else:
            top = 80000

        if(self.can_move_right()):
            right = self.count_heuristic_from_a_to_b(x+1, y, nearest_trash[0], nearest_trash[1])
        else:
            right = 80000


        moves = {'bottom': bottom, 'left': left, 'top': top, 'right': right}

        d = sorted(moves, key=moves.__getitem__)

        print(moves)

        print(d)
        print("Najbliższy trash:", nearest_trash)
        print("wartosc x:", x)
        print("wartosc y:", y)

        moves = {'bottom': bottom, 'left': left, 'top': top, 'right': right}

        d = sorted(moves, key=moves.__getitem__)

        if(d[0] == 'bottom' and bottom == left):
            if(self.count_route_wage_vertically_down(x, y+1, current_grid) > self.count_route_wage_horizontally_left(x-1, y, current_grid)):
                bottom = bottom - 500
            elif(self.count_route_wage_vertically_down(x, y+1, current_grid) < self.count_route_wage_horizontally_left(x-1, y, current_grid)):
                left = left - 500
            else:
                left = left-500

        if(d[0] == 'bottom' and bottom == right):
            if(self.count_route_wage_vertically_down(x, y+1, current_grid) > self.count_route_wage_horizontally_right(x+1, y, current_grid)):
                bottom = bottom - 500
            elif(self.count_route_wage_vertically_down(x, y+1, current_grid) < self.count_route_wage_horizontally_right(x+1, y, current_grid)):
                right = right - 500
            else:
                right = right - 500

        if(d[0] == 'bottom' and bottom == top):
            if(self.count_route_wage_vertically_down(x, y+1, current_grid) > self.count_route_wage_vertically_top(x, y-1, current_grid)):
                bottom = bottom - 500
            elif(self.count_route_wage_vertically_down(x, y+1, current_grid) < self.count_route_wage_vertically_top(x, y-1, current_grid)):
                top = top - 500

        if(d[0] == 'top' and bottom == top):
            if(self.count_route_wage_vertically_down(x, y+1, current_grid) > self.count_route_wage_vertically_top(x, y-1, current_grid)):
                bottom = bottom - 500
            elif(self.count_route_wage_vertically_down(x, y+1, current_grid) < self.count_route_wage_vertically_top(x, y-1, current_grid)):
                top = top - 500

        if(d[0] == 'top' and left == top):
            if(self.count_route_wage_vertically_top(x, y-1, current_grid) > self.count_route_wage_horizontally_left(x-1, y, current_grid)):
                top = top - 500
            elif(self.count_route_wage_vertically_top(x, y-1, current_grid) < self.count_route_wage_horizontally_left(x-1, y, current_grid)):
                left = left - 500
            else:
                left = left - 500

        if(d[0] == 'top' and right == top):
            if(self.count_route_wage_vertically_top(x, y-1, current_grid) > self.count_route_wage_horizontally_right(x+1, y, current_grid)):
                top = top - 500
            elif(self.count_route_wage_vertically_top(x, y-1, current_grid) < self.count_route_wage_horizontally_right(x+1, y, current_grid)):
                right = right - 500
            else:
                right = right - 500

        if(d[0] == 'left' and left == bottom):
            if(self.count_route_wage_horizontally_left(x-1, y, current_grid) > self.count_route_wage_vertically_down(x, y+1, current_grid)):
                left = left - 500
            elif(self.count_route_wage_horizontally_left(x-1, y, current_grid) < self.count_route_wage_vertically_down(x, y+1, current_grid)):
                bottom = bottom - 500
            else:
                left = left - 500

        if(d[0] == 'left' and left == top):
            if(self.count_route_wage_horizontally_left(x-1, y, current_grid) > self.count_route_wage_vertically_top(x, y-1, current_grid)):
                left = left - 500
            elif(self.count_route_wage_horizontally_left(x-1, y, current_grid) < self.count_route_wage_vertically_top(x, y-1, current_grid)):
                top = top - 500
            else:
                left = left - 500

        if(d[0] == 'left' and left == right):
            if(self.count_route_wage_horizontally_left(x-1, y, current_grid) > self.count_route_wage_horizontally_right(x+1, y, current_grid)):
                left = left - 500
            elif(self.count_route_wage_horizontally_left(x-1, y, current_grid) < self.count_route_wage_horizontally_right(x+1, y, current_grid)):
                right = right - 500

        if(d[0] == 'right' and right == bottom):
            if(self.count_route_wage_horizontally_right(x+1, y, current_grid) > self.count_route_wage_vertically_down(x, y+1, current_grid)):
                right = right - 500
            elif(self.count_route_wage_horizontally_right(x+1, y, current_grid) < self.count_route_wage_vertically_down(x, y+1, current_grid)):
                bottom = bottom - 500
            else:
                right = right - 500

        if(d[0] == 'right' and right == top):
            if(self.count_route_wage_horizontally_right(x+1, y, current_grid) > self.count_route_wage_vertically_top(x, y-1, current_grid)):
                right = right - 500
            elif(self.count_route_wage_horizontally_right(x+1, y, current_grid) < self.count_route_wage_vertically_top(x, y-1, current_grid)):
                top = top - 500
            else:
                right = right - 500

        if(d[0] == 'right' and right == left):
            if(self.count_route_wage_horizontally_right(x+1, y, current_grid) > self.count_route_wage_horizontally_left(x-1, y, current_grid)):
                right = right - 500
            elif(self.count_route_wage_horizontally_right(x+1, y, current_grid) < self.count_route_wage_horizontally_left(x-1, y, current_grid)):
                left = left - 500

        print(recent_move)

        if(recent_move == 'left'):
            right = right + 600

        if(recent_move == 'right'):
            left = left + 600

        if(recent_move == 'bottom'):
            top = top + 600

        if(recent_move == 'top'):
            bottom = bottom + 600

        moves = {'bottom': bottom, 'left': left, 'top': top, 'right': right}

        d = sorted(moves, key=moves.__getitem__)

        print("po zabiagech:")
        print(moves)

        print(d)

        if(d[0] == 'bottom'):
            possible_moves.append(Move.MOVE_DOWN)
        elif(d[0] == 'top'):
            possible_moves.append(Move.MOVE_TOP)
        elif(d[0] == 'right'):
            possible_moves.append(Move.MOVE_RIGHT)
        elif(d[0] == 'left'):
            possible_moves.append(Move.MOVE_LEFT)



        print("Z funkcji ruchup", possible_moves)

        return possible_moves

    #####################################################

    def collect_trash(self, trash_to_collect):
        trash_to_collect.empty_bin()

    def move_left(self):
        if not self.move_to(self.current_position_x-1, self.current_position_y):
            return False

    def move_right(self):
        if not self.move_to(self.current_position_x+1, self.current_position_y):
            return False

    def move_top(self):
        if not self.move_to(self.current_position_x, self.current_position_y-1):
            return False

    def move_down(self):
        if not self.move_to(self.current_position_x, self.current_position_y+1):
            return False

    def can_move_left(self):
        return self.can_move_to(self.current_position_x-1, self.current_position_y)

    def can_move_right(self):
        return self.can_move_to(self.current_position_x+1, self.current_position_y)

    def can_move_top(self):
        return self.can_move_to(self.current_position_x, self.current_position_y-1)

    def can_move_down(self):
        return self.can_move_to(self.current_position_x, self.current_position_y+1)

    def possible_moves(self):
        possible_moves = []
        if self.can_move_left():
            possible_moves.append(Move.MOVE_LEFT)
        if self.can_move_down():
            possible_moves.append(Move.MOVE_DOWN)
        if self.can_move_right():
            possible_moves.append(Move.MOVE_RIGHT)
        if self.can_move_top():
            possible_moves.append(Move.MOVE_TOP)
        return possible_moves

    def possible_cord(self):
        possible_cord = []
        if self.can_move_left():
            possible_cord.append((self.current_position_x-1,self.current_position_y))
        if self.can_move_down():
            possible_cord.append((self.current_position_x,self.current_position_y+1))
        if self.can_move_right():
            possible_cord.append((self.current_position_x+1,self.current_position_y))
        if self.can_move_top():
            possible_cord.append((self.current_position_x,self.current_position_y-1))
        return possible_cord

    def make_move(self,move):
        if move == Move.MOVE_LEFT:
            self.move_left()
        elif move == Move.MOVE_DOWN:
            self.move_down()
        elif move == Move.MOVE_RIGHT:
            self.move_right()
        elif move == Move.MOVE_TOP:
            self.move_top()

    def move_to(self, x, y):
        if not self.can_move_to(x, y):
            return False

        if x > self.current_position_x:
            self.offset_y = 9
            self.offset_x = 0
            self.type = 'truck_right'
        elif x < self.current_position_x:
            self.offset_y = 9
            self.offset_x = 0
            self.type = 'truck_left'
        elif y > self.current_position_y:
            self.offset_y = 0
            self.offset_x = 9
            self.type = 'truck_down'
        elif y < self.current_position_y:
            self.offset_y = 0
            self.offset_x = 9
            self.type = 'truck_top'
        self.set_current_position_x(x)
        self.set_current_position_y(y)