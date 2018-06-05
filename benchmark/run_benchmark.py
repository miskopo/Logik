import pandas as pd
from controller.controller_unit import Controller
from click import progressbar

class Benchmark:
    def __init__(self, arg_parser):
        self.results = pd.DataFrame(columns=['Solver name', 'Wins', 'Attempts'])
        self.args = arg_parser

    def __call__(self, *args, **kwargs):
        self.generate_data()
        self.process_data()
        self.save_data_output()

    def generate_data(self):
        # TODO: Separate tests into four lengths and plot it as subplots or whatever, I don't care
        
        for solver in Controller.solvers:
            with progressbar(
                    range(self.args.number_of_tests),
                    show_percent=True,
                    show_eta=True,
                    label="Running benchmark for {}:\t".format(Controller.solvers[solver].__name__)) as bar:
                for i in bar:
                    game = Controller(
                        solver,
                        self.args,
                        number_of_colors=self.args.number_of_colors,
                        attempts=self.args.attempts,
                        pattern_size=self.args.pattern_size)
                    result = game()
                    self.results = self.results.append(
                        pd.DataFrame([[Controller.solvers[solver].__name__,
                                       result[0],
                                       result[1]]],
                                     columns=self.results.columns), ignore_index=True)

    def process_data(self):
        self.results = self.results.loc[self.results['Wins']]
        del self.results['Wins']
        self.results['Attempts'] = pd.to_numeric(self.results['Attempts'])
        self.results = self.results.groupby('Solver name').mean()

    def save_data_output(self):
        # print(self.results)
        plot = self.results.plot(kind='bar',
                                 title="Average of attempts needed to solve game",
                                 grid=True,
                                 rot=0,
                                 legend=False)
        fig = plot.get_figure()
        fig.savefig('view/graph.png')