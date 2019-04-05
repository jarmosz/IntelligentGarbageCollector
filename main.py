import map
import truck

map = map.Map()

map.generate_grid()
map.render_window()

truck = truck.Truck(map)

i = 0

while(True):
    truck.set_current_map_state(map.get_grid())
    map.get_truck_current_position_on_the_grid(truck)
    map.update_window()
    if(map.grid[truck.get_current_position_y()][truck.get_current_position_x()].get_type() == "cross_road"):
        truck.move_to(truck.get_current_position_x(), truck.get_current_position_y()+1)
    else:
        truck.move_to(truck.get_current_position_x() + 1, truck.get_current_position_y())