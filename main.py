import random
import sys
import map
import truck
import copy
from moves import Move
from dfs import DeepFirstSearch
from a_star import BestFirstSearch
from bfs import BreathFirstSearch
_map = map.Map()
move_list = []

_map.generate_grid()
# _map.import_map()
truck = truck.Truck(_map)
truck.set_current_map_state(_map.get_grid())
_map.set_truck_current_position_on_the_grid(truck)


# changing trash_emty to trash_yellow
for i in _map.grid:
    for j in i:
        if j.get_type() == 'empty_trash' and random.randrange(0, 10) > 0:
            j.type = "yellow_trash"

#move_list = DeepFirstSearch().start_dfs(_map, 'yellow_trash')
#move_list = BestFirstSearch().start_A_star(_map, 'yellow_trash')
move_list = BreathFirstSearch().start_bfs(_map, 'yellow_trash')

print("Końcowa lista ruchów")

print(move_list)

j = 0
while(True):
    if len(move_list)-1 >= j:
        if move_list[j] == 'collect':
            pass
            tmp = truck.find_trash_around("yellow_trash")
            truck.collect_trash(tmp[0])
        else:
            #truck.make_move(move_list[j])
            truck.move_to(move_list[j][0], move_list[j][1])

        j = j+1

    _map.update_window()
    _map.render_window()
