class Road:
    def __init__(self, type):
        self.type = type
        self.texture = ''
        self.set_texture()
    
    def set_texture(self):
        if self.type == "horizontal_straight_road":
            self.texture = 'sprites/horizontal_straight_road.png'
        elif self.type == "vertical_straight_road":
            self.texture = 'sprites/vertical_straight_road.png'
        elif self.type == "cross_road":
            self.texture = 'sprites/crossroad.png'
    
    def get_texture(self):
        return self.texture

    def get_type(self):
        return self.type
    
