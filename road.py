import os
class Road:

    folder = os.path.dirname(os.path.realpath(__file__)) #get project's folder
    road_horizontal_path = os.path.join(folder,'sprites/horizontal_straight_road.png')
    road_vertical_path = os.path.join(folder,'sprites/vertical_straight_road.png')
    road_crossroad_path = os.path.join(folder,'sprites/crossroad.png')
    def __init__(self, type):
        self.type = type
        self.texture = ''
        
    def get_type(self):
        return self.type
    
