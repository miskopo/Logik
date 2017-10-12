from model.gameboard import Gameboard
from controller.brute_force import BruteForce

class Controller:
    def __init__(self, solving_algorithm_name):
        self.gameboard = Gameboard()
        self.gameboard.generate_pattern()
        if solving_algorithm_name == "bruteforce":
            self.solver = BruteForce(self.gameboard.pattern_size, self.gameboard.colors)

    def __call__(self, *args, **kwargs):
        pass

    def guess_pattern(self):
        return self.solver.guess_pattern()

    def evaluate_guessed_pattern(self):
        pass

    def make_one_turn(self):
        self.gameboard.guessed = self.guess_pattern()
        self.gameboard.evaluation = self.evaluate_guessed_pattern()


    def run_game(self):
        pass