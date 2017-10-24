from argparse import ArgumentParser


def init_parser():
    parser = ArgumentParser()
    parser.add_argument("-v",
                        "--verbose",
                        help="Enable output printing",
                        action="store_true",
                        default=None)
    parser.add_argument("-i",
                        "--interactive",
                        help="Run game in interactive human playable mode",
                        action="store_true",
                        default=None)
    parser.add_argument("-b",
                        "--benchmark",
                        help="Run test and benchmark of solving algorithms.",
                        action="store_true",
                        default=None)
    parser.add_argument("-n",
                        "--number_of_tests",
                        help="Number if tests for benchmark.",
                        action="store",
                        type=int,
                        default=1000)
    parser.add_argument("--attempts",
                        help="Number of attempts for the solver.",
                        default=10000,
                        type=int,
                        action="store")
    parser.add_argument("--number_of_colors",
                        help="Number of colors to generate pattern with.",
                        type=int,
                        default=8,
                        action="store")
    parser.add_argument("--pattern_size",
                        help="Pattern size to be generated",
                        type=int,
                        default=5,
                        action="store")
    return parser.parse_args()
