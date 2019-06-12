from vowpalwabbit import pyvw
import grass
import road
import trash 
import map
import truck
from moves import Move
import random
square_size = 5
half_square_size = square_size//2
MAP_RESOLUTION = 10

two_last_wage = -11111
last_wage = -11111
def my_predict(vw, s):
    ex = vw.example(s)
    pp = 0.
    for f,v in ex.iter_features():
        pp += vw.get_weight(f) * v
    return pp
def randomize_move(wage):
    global last_wage
    global two_last_wage
    two_last_wage = last_wage
    tmp = random.uniform(0,4)
    wage = tmp
    last_wage = wage
    return calculate_move(wage)
#q = my_predict(vw,a)
def calculate_move(wage):
    if wage >= 1.5 and wage <= 2.4:
        return 'collect'
    elif wage >=2.4 and wage <=3.3:
        return Move.MOVE_LEFT
    elif wage >=3.3:
        return Move.MOVE_RIGHT
    elif wage <=0.5:
        return Move.MOVE_TOP
    elif wage >=0.5 and wage <=1.5:
        return Move.MOVE_DOWN
    
def predict_move(map):
    zeros = [ [0] * square_size for _ in range(square_size)]
    y = map.truck.current_position_x # 
    x = map.truck.current_position_y
    print(x,y)
    for i in range(-half_square_size,half_square_size+1):
        for j in range(-half_square_size,half_square_size+1):
            if x+i>=0 and y+j >=0 and x+i<MAP_RESOLUTION and y+j<MAP_RESOLUTION:
                if isinstance(map.grid[x+i][y+j],road.Road):
                    zeros[2+i][2+j] = 1
                elif isinstance(map.grid[x+i][y+j],trash.Trash):
                    if map.grid[x+i][y+j].type == 'empty_trash':
                        zeros[2+i][2+j] = 2
                    else:   
                        zeros[2+i][2+j] = 3
    state = ' '
    index = 0
    for rows in zeros:
        for value in rows:
            state += ''.join('f{}:{} '.format(index, value))
            index += 1
            #print(state)
    vision = ("{} | {}\n".format(str('1'), state))
    print(vision)
    global last_wage
    global two_last_wage
    wage = my_predict(vw,vision)

    print(wage,last_wage,two_last_wage)
    if last_wage == wage or two_last_wage == wage:
        return randomize_move(wage)
    two_last_wage = last_wage
    last_wage = wage
    print(wage)
    move = calculate_move(wage)
    print(move)
    return move





vw = pyvw.vw("--quiet -i trained_5")
_map = map.Map(10)
move_list = []
#_map.generate_grid()
#_map.import_map()
truck = truck.Truck(_map)
truck.set_current_map_state(_map.get_grid())
_map.set_truck_current_position_on_the_grid(truck)
#define_square(_map)
predict_move(_map)
while(True):
    move = predict_move(_map)
    _map.truck.make_move(move)
    _map.update_window()
    _map.render_window()


