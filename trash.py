from random import randint
import random
import os
class Trash:
    folder = os.path.dirname(os.path.realpath(__file__)) #get project's folder
    trash_yellow_path = os.path.join(folder,'sprites/yellow.png')
    trash_empty_path = os.path.join(folder,'sprites/empty.png')
    trash_blue_path = os.path.join(folder,'sprites/blue.jpg')
    trash_red_path = os.path.join(folder,'sprites/red.png')

    def __init__(self, type):
        self.type = type
        self.capacity = randint(1, 100)
    

    def empty_bin(self):
        self.type = 'empty_trash'
        self.capacity = 0
        
    def get_type(self):
        return self.type

    def get_capacity(self):
        return self.capacity