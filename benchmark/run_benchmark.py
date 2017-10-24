from controller.controller_unit import Controller
from click import progressbar


class Benchmark:
    def __init__(self, arg_parser):
        self.results = []
        self.args = arg_parser

    def __call__(self, *args, **kwargs):
        for solver in Controller.solvers:
            with progressbar(
                    range(self.args.number_of_tests),
                    show_percent=True,
                    show_eta=True,
                    label="Running benchmark for {}\t: ".format(Controller.solvers[solver].__name__)) as bar:
                for _ in bar:
                    game = Controller(
                        solver,
                        self.args,
                        number_of_colors=self.args.number_of_colors,
                        attempts=self.args.attempts,
                        pattern_size=self.args.pattern_size)
                    self.results.append((Controller.solvers[solver].__name__, game()))
        # print(self.results)
