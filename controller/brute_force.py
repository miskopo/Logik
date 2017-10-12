"""
:author: Michal Polovka
"""
from controller.solving_algorithm import SolvingAlgorithm
from itertools import product

class BruteForce(SolvingAlgorithm):
    """
    Class represents Brute Force solving algorithm.
    """
    def __init__(self, pattern_size, colors):
        super().__init__(pattern_size, colors)

    def guess_pattern(self):
        # generate permutations of possible colors
        attack_list = [product(self.colors, repeat=self.pattern_size)]
        yield attack_list


