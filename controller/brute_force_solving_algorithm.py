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
        # Note: For pattern_size = 5 and number of colors = 8 there are 32,768 possibilities.
        if len(self.guessed) == 0:
            self.guessed = list(map(lambda x: list(x),
                                    list(product(self.colors, repeat=self.pattern_size))))[:self.attempts+1]

    def decide_next_step(self, evaluation, pattern_size):
        if evaluation == [str(1) for _ in range(pattern_size)]:
            return "finish"
        else:
            return "continue"



