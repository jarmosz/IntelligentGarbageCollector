from Node import Node
class GrassNode(Node):
    cell_size = 0
    image = 1 # here goes sprite to display just for now let's set it to 1
    IMAGE_1 = 1 # here goes first image .. e.g. IMAGE_2  = 'grass.jpg'

    def __init__(self,position):
        pass # randomize grass sprite
        cell_size = Node.cell_size
