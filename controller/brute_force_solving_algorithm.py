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
        """
        Generate feasible region for this type of algorithm.
        :return: None, result is stored in attribute of this class.
         """
        # generate cartesian product of possible colors
        # Note: For pattern_size = 5 and number of colors = 8 there are 32,768 possibilities.
        if len(self.guessed) == 0:
            self.guessed = list(map(lambda x: list(x),
                                    list(product(self.colors, repeat=self.pattern_size))))[:self.attempts+1]

    def decide_next_step(self, evaluation, pattern_size, iteration):
        """
        Method decides next step in solving strategy in consideration of given evaluation of previous guess.
        :param iteration: not needed in this type of algorithm
        :param evaluation: evaluation of previous guess done by gameboard
        :param pattern_size: size of the guessed pattern
        :return: string designating whether to continue or end game
        """
        if evaluation == [str(1) for _ in range(pattern_size)]:
            return "finish"
        else:
            return "continue"



