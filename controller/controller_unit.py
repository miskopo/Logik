from model.gameboard import Gameboard
from controller.brute_force_solving_algorithm import BruteForce
from controller.true_random_solving_algorithm import TrueRandom
from controller.single_color_solving_algorithm import SingleColor
from controller.semi_random_solving_algorithm import SemiRandom
from arg_parser import init_parser


class Controller:
    def __init__(self, solving_algorithm_name, arg_parser, number_of_colors=8, attempts=1000, pattern_size=5, ):
        self.args = arg_parser
        if attempts > number_of_colors**pattern_size:
            attempts = number_of_colors ** pattern_size
        self.gameboard = Gameboard(attempts=attempts, number_of_colors=number_of_colors, pattern_size=pattern_size)
        self.gameboard.generate_pattern()
        self.guessed = []
        self.solvers = {
            "brute_force": BruteForce,
            "true_random": TrueRandom,
            "single_color": SingleColor,
            "semi_random": SemiRandom
        }
        self.solver = self.solvers[solving_algorithm_name](pattern_size=self.gameboard.pattern_size,
                                                           colors=self.gameboard.colors,
                                                           attempts=self.gameboard.attempts)

    def __call__(self, *args, **kwargs):
        self.run_game()

    def guess_pattern(self):
        self.solver.guess_pattern()
        return self.solver.guessed

    def make_one_turn(self, iteration):
        try:
            self.gameboard.guessed = self.guess_pattern()[iteration]
            self.gameboard.evaluate_guess()
        except IndexError:
            print("Solver run out of guesses.")
            self.end_game(iteration, self.gameboard.pattern, False)
            exit(0)

    def run_game(self):
        print()
        for iteration in range(self.gameboard.attempts):
            self.make_one_turn(iteration)
            action = self.solver.decide_next_step(self.gameboard.evaluation, iteration)
            if action == "finish":
                self.end_game(iteration, self.gameboard.pattern, solver_won=True)
                break
            elif action == "continue":
                continue
            elif len(action) == 2:
                self.gameboard.attempts = len(action[1])**self.gameboard.pattern_size
                self.solver = self.solvers[action[0]](pattern_size=self.gameboard.pattern_size,
                                                      colors=action[1],
                                                      attempts=self.gameboard.attempts)
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
        return solver_won


parser = init_parser()
game = Controller("single_color", parser, attempts=10000)
game()
