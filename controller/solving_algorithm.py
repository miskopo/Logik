"""
:author: Michal Polovka
"""
from abc import ABCMeta


class SolvingAlgorithm:
    """
    Meta class representing general solving algorithm
    """

    def __init__(self, pattern_size, colors):
        self.pattern_size = pattern_size
        self.colors = colors

    def guess_pattern(self):
        pass

    def assess_evaluation(self):
        pass
    
    def decide_next_step(self):
        pass


