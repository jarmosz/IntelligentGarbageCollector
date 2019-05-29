import os
class Grass:
    folder = os.path.dirname(os.path.realpath(__file__)) #get project's folder
    grass_path = os.path.join(folder,'sprites/grass.png')
    
    type = "grass"
    def __init__(self):
        pass
    
    def get_type(self):
        return self.type

    
