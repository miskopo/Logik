"""
:author: Michal Polovka
"""


class SolvingAlgorithm:
    """
    Abstract class representing general solving algorithm
    """

    def __init__(self, pattern_size, colors, attempts):
        self.pattern_size = pattern_size
        self.colors = colors
        self.attempts = attempts

    def guess_pattern(self):
        pass

    def decide_next_step(self, evaluation, iteration):
        pass


