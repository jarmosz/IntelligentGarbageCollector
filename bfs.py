import map
import truck
import copy
from moves import Move
import sys
type_of_trash = None
move_list = []
s = 0
sys.setrecursionlimit(12000)
class BreathFirstSearch:
    def start_bfs(self, _map,  _type_of_trash):
        global type_of_trash
        type_of_trash = _type_of_trash
        starting_pos = ((_map.truck.get_current_position_x(),
                        _map.truck.get_current_position_y()))
        map = copy.deepcopy(_map)
        self.bfs_shortest_path(map, starting_pos, _map.truck.find_next_trash_to_visit('yellow_trash'))
        return move_list

    def bfs_shortest_path(self, map, start, goal):
        global move_list
        if self.check_if_is_done(map):
            print("done")
            return
        explored = []
        queue = [[start]]
        if move_list == [] or move_list[-1] == 'collect':
            self.find_trash_around(start[0], start[1], map, [(start)])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            map.truck.move_to(node[0], node[1])
            if node not in explored:
                possible_cord = map.truck.possible_cord()
                for i in possible_cord:
                    new_path = list(path)
                    new_path.append(i)
                    queue.append(new_path)
                    explored.append(node)
                    self.find_trash_around(i[0], i[1], map, new_path)


    def check_if_is_done(self,m):
        for i in m.grid:
            for j in i:
                if j.get_type() == type_of_trash:
                    return False
        return True

    def find_trash_around(self, x, y, map, new_path):
        global move_list
        trash_around = map.truck.find_trash(type_of_trash, x, y)
        if trash_around != []:
            tmp = map.truck.find_trash(type_of_trash, x, y)
            trash_to_collect = tmp[0]
            map.truck.collect_trash(trash_to_collect)
            move_list += new_path[1:]
            move_list.append("collect")
            self.bfs_shortest_path(map,  new_path[-1], map.truck.find_next_trash_to_visit('yellow_trash') )
