"""
:author: Michal Polovka
"""
from controller.solving_algorithm import SolvingAlgorithm


class TrueRandom(SolvingAlgorithm):
    def __init__(self, pattern_size, colors, attempts):
        super().__init__(pattern_size, colors, attempts)
        self.guessed = []

    def guess_pattern(self):
        pass