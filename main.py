import map2

map = map2.Map()

map.generate_grid()
map.render_window()

while(True):
    map.update_window()