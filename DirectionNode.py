class DirectionNode: #abstract class only to derive from
    def __init__(self):
        pass

    def __init__(self,left_node,top_node,right_node,bottom_node):
        self.left_node = left_node
        self.right_node = right_node
        self.bottom_node = bottom_node
        self.top_node = top_node
