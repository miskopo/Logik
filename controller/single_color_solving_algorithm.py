"""
:author: Michal Polovka
"""
from controller.solving_algorithm import SolvingAlgorithm


class SingleColor(SolvingAlgorithm):
    def __init__(self, pattern_size, colors, attempts):
        super().__init__(pattern_size, colors, attempts)
        self.guessed = []

    def guess_pattern(self):
        if len(self.guessed) == 0:
            self.guessed = [self.pattern_size * str(i).split() for i in self.colors]

    def decide_next_step(self, evaluation, iteration):
        if evaluation == [str(1) for _ in range(self.pattern_size)]:
            return "finish"
        elif '-1' in evaluation:
            last_guess = self.guessed[iteration]
            bad_color = last_guess[evaluation.index('-1')]
            if int(bad_color) in self.colors:
                self.colors.remove(int(bad_color))
            self.guessed = []
            return "continue"
        else:
            return "brute_force", self.colors

