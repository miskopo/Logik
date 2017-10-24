from argparse import ArgumentParser


def init_parser():
    parser = ArgumentParser()
    parser.add_argument("-v",
                        "--verbose",
                        help="Enable output printing",
                        action="store_true")
    parser.add_argument("-i",
                        "--interactive",
                        help="Run game in interactive human playable mode",
                        action="store_true")
    return parser.parse_args()