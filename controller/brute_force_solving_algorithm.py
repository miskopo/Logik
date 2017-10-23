"""
:author: Michal Polovka
"""
from controller.solving_algorithm import SolvingAlgorithm
from itertools import product


class BruteForce(SolvingAlgorithm):
    """
    Class represents Brute Force solving algorithm.
    """
    def __init__(self, pattern_size, colors, attempts):
        super().__init__(pattern_size, colors, attempts)
        self.guessed = []

    def guess_pattern(self):
        # generate cartesian product of possible colors
        if len(self.guessed) == 0:
            self.guessed = list(map(lambda x: list(x), list(product(self.colors, repeat=self.pattern_size)))[:self.attempts])
        return self.guessed

    def decide_next_step(self, evaluation, pattern_size):
        if evaluation == [str(1) for _ in range(pattern_size)]:
            return "finish"
        else:
            return "continue"



