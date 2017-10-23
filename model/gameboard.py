"""
:author: Michal Polovka
"""
from controller.brute_force_solving_algorithm import BruteForce
from random import randint


class Gameboard:
    """
    Class representing gameboard consisting of guessed pattern,
    status field and possible colors to choose from.
    """

    def __init__(self, number_of_colors=8, pattern_size=5, attempts=12):
        self.number_of_colors = number_of_colors
        self.pattern_size = pattern_size
        self.attempts = attempts
        self.colors = list(range(0, number_of_colors))  # colors are represented by numbers as they are not being shown here
        self.pattern = []
        self.guessed = []
        self.evaluation = []

    def generate_pattern(self):
        # self.pattern = (4,4,4,4,4)
        # chosen by fair dice roll
        # guaranteed to be random
        self.pattern = "".join(
            str(randint(0, self.number_of_colors))
            for _ in range(0, self.pattern_size))

    def evaulate_guess(self):
        pass
