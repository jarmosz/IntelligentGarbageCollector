from random import randint
import random

class Trash:

    def __init__(self, type):
        self.type = type
        self.texture = ''
        self.set_texture()
        self.capacity = randint(1, 1000)
    
    def set_texture(self):
        if self.type == "empty_trash":
            self.texture = 'sprites/empty.png'
        elif self.type == "yellow_trash":
            self.texture = 'sprites/yellow.png'
        elif self.type == "blue_trash":
            self.texture = 'sprites/blue.jpg'
        elif self.type == "red_trash":
            self.texture = 'sprites/red.png'
    
    def get_texture(self):
        return self.texture

    def get_type(self):
        return self.type

    def get_capacity(self):
        return self.capacity