from model.gameboard import Gameboard
import arg_parser
from controller.brute_force_solving_algorithm import BruteForce
from controller.true_random_solving_algorithm import TrueRandom
from controller.single_color_solving_algorithm import SingleColor
from controller.semi_random_solving_algorithm import SemiRandom


class Controller:
    def __init__(self, solving_algorithm_name, arg_parser, attempts=1000):
        self.args = arg_parser
        self.gameboard = Gameboard(attempts=attempts)
        self.gameboard.generate_pattern()
        self.guessed = []
        solver = {
            "brute_force": BruteForce,
            "true_random": TrueRandom,
            "single_color": SingleColor,
            "semi_random": SemiRandom
        }
        self.solver = solver[solving_algorithm_name](pattern_size=self.gameboard.pattern_size,
                                                     colors=self.gameboard.colors,
                                                     attempts=self.gameboard.attempts)

    def __call__(self, *args, **kwargs):
        self.run_game()

    def guess_pattern(self):
        self.solver.guess_pattern()
        return self.solver.guessed

    def make_one_turn(self, iteration=0):
        self.gameboard.guessed = self.guess_pattern()[iteration]
        self.gameboard.evaluate_guess()

    def run_game(self):
        print()
        for iteration in range(self.gameboard.attempts):
            self.make_one_turn(iteration)
            action = self.solver.decide_next_step(self.gameboard.evaluation, self.gameboard.pattern_size)
            if action == "finish":
                self.end_game(iteration, self.gameboard.pattern, solver_won=True)
                break
            elif action == "continue":
                continue
        else:
            self.end_game(self.gameboard.attempts, self.gameboard.pattern, solver_won=False)

    def end_game(self, iteration, pattern, solver_won):
        if self.args.verbose:
            print("The game ended in {} moves.\n Guessed pattern was {}\n Used solver: {}\n {} won.".format(
                iteration,
                "".join(pattern),
                str(self.solver.__class__.__name__),
                ("Solver" if solver_won else "Game")
            ))
        return True

