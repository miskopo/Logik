from model.gameboard import Gameboard
from controller.brute_force_solving_algorithm import BruteForce


class Controller:
    def __init__(self, solving_algorithm_name, attempts=1000):
        self.gameboard = Gameboard(attempts=attempts)
        self.gameboard.generate_pattern()
        self.guessed = []
        if solving_algorithm_name == "bruteforce":
            self.solver = BruteForce(pattern_size=self.gameboard.pattern_size,
                                     colors=self.gameboard.colors,
                                     attempts=self.gameboard.attempts)

    def __call__(self, *args, **kwargs):
        pass

    def guess_pattern(self):
        self.solver.guess_pattern()
        return self.solver.guessed

    # def evaluate_guessed_pattern(self):
    #     pass

    def make_one_turn(self, iteration=0):
        self.gameboard.guessed = self.guess_pattern()[iteration]
        self.gameboard.evaluate_guess()

    def run_game(self):
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
# controller = Controller("bruteforce", attempts=10000)
# controller.run_game()


