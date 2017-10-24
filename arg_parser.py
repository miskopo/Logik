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
    return parser.parse_args()