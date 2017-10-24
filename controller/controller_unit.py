from model.gameboard import Gameboard
from controller.brute_force_solving_algorithm import BruteForce
from controller.true_random_solving_algorithm import TrueRandom
from controller.single_color_solving_algorithm import SingleColor
from controller.semi_random_solving_algorithm import SemiRandom


class Controller:
    def __init__(self, solving_algorithm_name, attempts=1000):
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
        pass

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

    @staticmethod
    def end_game(iteration, pattern, solver_won):
        print("The game ended in {} moves.\n Guessed pattern was {}\n {} won.".format(
            iteration,
            "".join(pattern),
            ("Solver" if solver_won else "Game")
        ))
        return True


# temporary solution
controller = Controller("brute_force", attempts=32768)
controller.run_game()
