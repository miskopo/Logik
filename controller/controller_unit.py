from model.gameboard import Gameboard
from controller.brute_force_solving_algorithm import BruteForce


class Controller:
    def __init__(self, solving_algorithm_name):
        self.gameboard = Gameboard()
        self.gameboard.generate_pattern()
        if solving_algorithm_name == "bruteforce":
            self.solver = BruteForce(self.gameboard.pattern_size, self.gameboard.colors, self.gameboard.attempts)

    def __call__(self, *args, **kwargs):
        pass

    def guess_pattern(self):
        return self.solver.guess_pattern()

    # def evaluate_guessed_pattern(self):
    #     pass

    def make_one_turn(self, iteration=0):
        self.gameboard.guessed = self.guess_pattern()[iteration]
        self.gameboard.evaluate_guess()
        print(self.gameboard.evaluation)

    def run_game(self):
        pass
