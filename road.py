class Road:
    def __init__(self, node_type):
        self.node_type = node_type
        self.texture = ''
        self.set_texture()
    
    def set_texture(self):
        if self.node_type == "horizontal_straight_road":
            self.texture = 'sprites/horizontal_straight_road.png'
        elif self.node_type == "vertical_straight_road":
            self.texture = 'sprites/vertical_straight_road.png'
        elif self.node_type == "cross_road":
            self.texture = 'sprites/crossroad.png'
    
    def get_texture(self):
        return self.texture

    def get_node_type(self):
        return self.node_type
    
