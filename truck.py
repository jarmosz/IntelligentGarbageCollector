import map
import os
import math
from moves import Move
class Truck:

    folder = os.path.dirname(os.path.realpath(__file__)) #get project's folder
    truck_right_path = os.path.join(folder,'sprites/truck_right.png')
    truck_left_path = os.path.join(folder,'sprites/truck_left.png')
    truck_top_path = os.path.join(folder,'sprites/truck_top.png')
    truck_down_path = os.path.join(folder,'sprites/truck_down.png')
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
        if x < len(self.grid[0]) and y < len(self.grid) and x>=0 and y>=0 :
            if (self.grid[y][x].get_type() == "horizontal_straight_road") or (self.grid[y][x].get_type() == "vertical_straight_road") or (self.grid[y][x].get_type() == "cross_road"):
                return True
        return False
    def find_trash_around(self,type):
        trash_list = []
        x = self.current_position_x
        y = self.current_position_y
       
        if x< len(self.grid[0])-1 and self.grid[y][x+1].get_type() == type  :
            trash_list.append(self.grid[y][x+1])
        if x> 0 and self.grid[y][x-1].get_type() == type and x:
            trash_list.append(self.grid[y][x-1])
        if y <len(self.grid)-1 and self.grid[y+1][x].get_type() == type:
            trash_list.append(self.grid[y+1][x])
        if y>0 and self.grid[y-1][x].get_type() == type and y >=0 :
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


    def find_next_trash_to_visit(self,type):
        not_visited_trashes = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].get_type() == "yellow_trash":
                    pom_list = []
                    pom_list.append(j);
                    pom_list.append(i)
                    not_visited_trashes.append(pom_list)

        x = self.get_current_position_x();
        y = self.get_current_position_y();

        #Heuristic, we want to know which empty trash is nearest to the truck position in this state.

        measure = 100.0;
        nearest_trash = [];
        for trash in not_visited_trashes:
            next_measure = math.sqrt((x - trash[0])**2 + (y - trash[1])**2)
            if(next_measure < measure):
                measure = next_measure
                nearest_trash = trash[:]
        
        return nearest_trash


    def generate_possible_moves_to_achieve_nearest_trash(self, nearest_trash):
        x = self.get_current_position_x();
        y = self.get_current_position_y();

        possible_moves = []

        if x < nearest_trash[0]:
            if self.can_move_right():
                possible_moves.append(Move.MOVE_RIGHT)

        elif x > nearest_trash[0]:
            if self.can_move_left():
                possible_moves.append(Move.MOVE_LEFT)

        elif x == nearest_trash[0] and y < nearest_trash[1]:
            if self.can_move_down():
                possible_moves.append(Move.MOVE_DOWN)

        elif x == nearest_trash[0] and y > nearest_trash[1]:
            if self.can_move_top():
                possible_moves.append(Move.MOVE_TOP)

        return possible_moves




    def collect_trash(self,trash_to_collect):
        trash_to_collect.empty_bin()
        

    def move_left(self):
        if not self.move_to(self.current_position_x-1,self.current_position_y):
            return False
    
    def move_right(self):
        if not self.move_to(self.current_position_x+1,self.current_position_y):
            return False
    
    def move_top(self):
        if not self.move_to(self.current_position_x,self.current_position_y-1):
            return False
    
    def move_down(self):
        if not self.move_to(self.current_position_x,self.current_position_y+1):
            return False
    
    def can_move_left(self):
        return self.can_move_to(self.current_position_x-1,self.current_position_y)

    def can_move_right(self):
        return self.can_move_to(self.current_position_x+1,self.current_position_y)

    def can_move_top(self):
        return self.can_move_to(self.current_position_x,self.current_position_y-1)

    def can_move_down(self):
        return self.can_move_to(self.current_position_x,self.current_position_y+1)

    
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
        if not self.can_move_to(x,y):
            return False
        
        if x>self.current_position_x:
            self.offset_y = 9
            self.offset_x = 0
            self.type = 'truck_right'
        elif x<self.current_position_x:
            self.offset_y = 9
            self.offset_x = 0
            self.type = 'truck_left'            
        elif y> self.current_position_y:
            self.offset_y = 0
            self.offset_x = 9
            self.type = 'truck_down'
        elif y<self.current_position_y:
            self.offset_y = 0
            self.offset_x = 9
            self.type = 'truck_top'
        self.set_current_position_x(x)
        self.set_current_position_y(y)        
        


    

