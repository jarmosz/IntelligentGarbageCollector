import map
import truck
import copy
import moves


_map = map.Map()
_map.import_map()
truck = truck.Truck(_map)
#
print("")


truck.set_current_map_state(_map.get_grid())
_map.set_truck_current_position_on_the_grid(truck)

q = copy.deepcopy(_map)
print(q,_map)

