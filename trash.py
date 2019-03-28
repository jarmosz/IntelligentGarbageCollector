from random import randint
import random

class Trash:

    def __init__(self, node_type):
        self.node_type = node_type
        self.texture = ''
        self.set_texture()
        self.capacity = randint(1, 1000)
    
    def set_texture(self):
        if self.node_type == "empty_trash":
            self.texture = 'sprites/empty.png'
        elif self.node_type == "yellow_trash":
            self.texture = 'sprites/yellow.png'
        elif self.node_type == "blue_trash":
            self.texture = 'sprites/blue.jpg'
        elif self.node_type == "red_trash":
            self.texture = 'sprites/red.png'
    
    def get_texture(self):
        return self.texture

    def get_node_type(self):
        return self.node_type

    def get_capacity(self):
        return self.capacity