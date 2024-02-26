from enum import Enum, auto

class Direction(Enum):
    stay = auto()
    right = auto()
    left = auto()
    down = auto()
    up = auto()
    no_direction = auto()