"""
:author: Michal Polovka
"""
from enum import Enum

class Gameboard:
    """
    Class representing gameboard consisting of guessed pattern, status field and possible colors to choose from.
    """
    def __init__(self, number_of_colors=8, pattern_size=5):
        self.number_of_colors = number_of_colors
        self.pattern_size = pattern_size


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    CYAN = 5
    WHITE = 6
    BLACK = 7
    VIOLET = 8


