import map
import truck
import copy
from moves import Move
from dfs import DeepFirstSearch
_map = map.Map()
import sys

move_list = []
    
#_map.generate_grid()
_map.import_map()
truck = truck.Truck(_map)
truck.set_current_map_state(_map.get_grid())
_map.set_truck_current_position_on_the_grid(truck)


#changing trash_emty to trash_yellow
for i in _map.grid:
    for j in i: 
        if j.get_type() == 'empty_trash':
            j.type = "yellow_trash"

move_list= DeepFirstSearch().start_dfs(_map,'yellow_trash')
print("Move List - ",move_list)

j = 0
while(True):
    if len(move_list)-1>= j:
        if move_list[j] == 'collect':
            pass
            tmp = truck.find_trash_around("yellow_trash")
            truck.collect_trash(tmp[0])
        else:
                truck.make_move(move_list[j])
        
        j=j+1
        

    _map.update_window() 
    _map.render_window()    #print(truck.can_move_left())
    # Added some simple movements test
    #if(_map.grid[truck.get_current_position_y()][truck.get_current_position_x()].get_type() == "cross_road"):
    #    truck.move_to(truck.get_current_position_x(), truck.get_current_position_y()+1)
    #else:
     #   truck.move_to(truck.get_current_position_x() + 1, truck.get_current_position_y())