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
        self.guessed = list(map(lambda x: list(x), list(product(self.colors, repeat=self.pattern_size))[:self.attempts]))
        return self.guessed

    def assess_evaluation(self, evaluation):
        pass

    def decide_next_step(self):
        pass



