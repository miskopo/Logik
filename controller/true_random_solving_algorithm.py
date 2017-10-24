"""
:author: Michal Polovka
"""
from controller.solving_algorithm import SolvingAlgorithm
from random import choice


class TrueRandom(SolvingAlgorithm):
    """
    True Random Solving Algorithm generates random sequences of given color till it wins (or attempts run out).
    Note, that generating of random number has very big (O) and can take several minutes to solve one game.
    """
    def __init__(self, pattern_size, colors, attempts):
        super().__init__(pattern_size, colors, attempts)
        self.guessed = []

    def guess_pattern(self):
        """
        Generate feasible region for this type of algorithm.
        :return: None, result is stored in attribute of this class.
        """
        if len(self.guessed) == 0:
            self.guessed = [[choice(self.colors) for _ in range(self.pattern_size)] for _ in range(self.attempts)]

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
