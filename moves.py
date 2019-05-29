from enum import Enum
class Move(Enum):
    MOVE_LEFT = 'move_left'
    MOVE_RIGHT = 'move_right'
    MOVE_TOP = 'move_top'
    MOVE_DOWN = 'move_down'
    COLLECT_LEFT = 'collect_down'
    COLLECT_RIGHT = 'collect_right'
    COLLECT_TOP = 'collect_top'
    COLLECT_BOTTOM = 'collect_bottom'
    
