"""
:author: Michal Polovka
"""
from controller.solving_algorithm import SolvingAlgorithm


class SingleColor(SolvingAlgorithm):
    def __init__(self, pattern_size, colors, attempts):
        super().__init__(pattern_size, colors, attempts)
        self.guessed = []

    def guess_pattern(self):
        self.guessed = [self.pattern_size * str(self.colors[i]).split() for i in self.colors][0:self.attempts]