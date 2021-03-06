"""
:author: Michal Polovka
"""
from random import randint


class Gameboard:
    """
    Class representing gameboard consisting of guessed pattern,
    status field and possible colors to choose from.
    """

    def __init__(self, number_of_colors, pattern_size, attempts):
        self.number_of_colors = number_of_colors
        self.pattern_size = pattern_size
        self.attempts = attempts
        # colors are represented by numbers as they are not being shown here
        self.colors = list(range(0, number_of_colors))
        self.pattern = []
        self.guessed = []
        self.evaluation = []

    def generate_pattern(self):
        # self.pattern = [4,4,4,4,4]
        # chosen by fair dice roll
        # guaranteed to be random (xkcd.com/221)
        self.pattern = [str(randint(0, self.number_of_colors-1)) for _ in range(0, self.pattern_size)]

    def evaluate_guess(self):
        self.evaluation = [
            "1" if str(x) == self.pattern[i] else "0" if str(x) in self.pattern else "-1"
            for i, x in enumerate(self.guessed)]
