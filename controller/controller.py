from model.gameboard import Gameboard


class Controller:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        gameboard = Gameboard()
        gameboard.generate_pattern()

    def guess_pattern(self, solving_algorithm_name):
        pass

    def evaluate_guessed_pattern(self):
        pass
