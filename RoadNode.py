import os
from DirectionNode import DirectionNode
cross_road_path = 'sprites\crossroad.png'
horizontal_stright_road = 'sprites\horizontal_straight_road.png'
vertical_stright_road = 'sprites\\vertical_straight_road.png'


class RoadNode(DirectionNode):

    def __init__(self):
        self.image = None
        self.position = None
        self.right_node = None
        self.left_node = None
        self.top_node = None
        self.bottom_node = None

    def choose_road_sprite(self):
        folder = os.path.dirname(os.path.realpath(__file__))

        if self.left_node != None and self.top_node != None:
            self.image = os.path.join(folder, cross_road_path)
        elif self.top_node != None or self.bottom_node != None:
            self.image = os.path.join(folder, vertical_stright_road)
        else:
            self.image = os.path.join(folder, horizontal_stright_road)
