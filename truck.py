import map

class Truck:

    def __init__(self, map):
        self.texture = 'sprites/truck_right.png'
        self.type = "truck"
        self.current_position_x = 0
        self.current_position_y = 0
        self.grid = map.grid
        self.set_starter_position_on_the_grid()
    
    def set_current_position_x(self, new_position_x):
        self.current_position_x = new_position_x

    def set_current_position_y(self, new_position_y):
        self.current_position_y = new_position_y

    def get_current_position_x(self):
        return self.current_position_x

    
    def get_current_position_y(self):
        return self.current_position_y

    

    def set_current_map_state(self, current_grid_grid):
        self.grid = current_grid_grid

    def set_starter_position_on_the_grid(self):
        for y in range(len(self.grid)):
            if self.grid[y][0].get_type() == "horizontal_straight_road":
                self.current_position_x = 0
                self.current_position_y = y
                break
        print(self.get_current_position_x())
        print(self.get_current_position_y())

    def get_type(self):
        return self.type

    def set_texture(self, texture):
        self.texture = texture

    def get_texture(self):
        return self.texture


    def can_move_to(self, x, y):
        if x < len(self.grid[0]) and y < len(self.grid):
            if (self.grid[y][x].get_type() == "horizontal_straight_road") or (self.grid[y][x].get_type() == "vertical_straight_road") or (self.grid[y][x].get_type() == "cross_road"):
                return True
            else:
                return False
        return False
    
    def move_to(self, x, y):

        if (self.can_move_to(x, y)) and (self.grid[y][x].get_type() == "horizontal_straight_road") and (self.get_current_position_x() < x):
            self.set_texture('sprites/truck_right.png')
            self.set_current_position_x(x)
            self.set_current_position_y(y)
         
        elif (self.can_move_to(x, y)) and (self.grid[y][x].get_type() == "horizontal_straight_road") and (self.get_current_position_x() > x):
            self.set_texture('sprites/truck_left.png')
            self.set_current_position_x(x)
            self.set_current_position_y(y)
           
        elif (self.can_move_to(x, y)) and (self.grid[y][x].get_type() == "vertical_straight_road") and (self.get_current_position_y() < y):
            self.set_texture('sprites/truck_down.png')
            self.set_current_position_x(x)
            self.set_current_position_y(y)
          
        elif (self.can_move_to(x, y)) and (self.grid[y][x].get_type() == "vertical_straight_road") and (self.get_current_position_y() > y):
            self.set_texture('sprites/truck_top.png')
            self.set_current_position_x(x)
            self.set_current_position_y(y)
          
        elif (self.can_move_to(x, y)) and (self.grid[y][x].get_type() == "cross_road") and (self.get_current_position_x() < x):
            self.set_texture('sprites/truck_right.png')
            self.set_current_position_x(x)
            self.set_current_position_y(y)
         
        elif (self.can_move_to(x, y)) and (self.grid[y][x].get_type() == "cross_road") and (self.get_current_position_x() > x):
            self.set_texture('sprites/truck_left.png')
            self.set_current_position_x(x)
            self.set_current_position_y(y)
       
        elif (self.can_move_to(x, y)) and (self.grid[y][x].get_type() == "cross_road") and (self.get_current_position_y() < y):
            self.set_texture('sprites/truck_down.png')
            self.set_current_position_x(x)
            self.set_current_position_y(y)
          
        elif (self.can_move_to(x, y)) and (self.grid[y][x].get_type() == "cross_road") and (self.get_current_position_y() > y):
            self.set_texture('sprites/truck_top.png')
            self.set_current_position_x(x)
            self.set_current_position_y(y)
        


    

