from controller.controller_unit import Controller
from colorama import Fore, init as fore_init
from arg_parser import init_parser
from benchmark.run_benchmark import Benchmark
fore_init()

args = init_parser()


def run():
    try:
        print(Fore.LIGHTGREEN_EX, "Welcome to the game Logik!", Fore.RESET)
        print("This implementation was created by Michal Polovka in 2017.\n"
              "Shareable under GPL-3.0 licence.\n"
              "See the game repository for details: https://github.com/miskopo/Logik")
        print()
        if args.interactive is None and args.benchmark is None:
            print(Fore.LIGHTYELLOW_EX, "You didn't choose whether you want to play or to run benchmark", Fore.RESET)
            print("0. Play the game!\n1. Run benchmark!")
            choice = -1
            while choice != '0' and choice != '1':
                choice = input("Your choice? ")
                if choice != '0' and choice != '1':
                    print(Fore.LIGHTRED_EX, "Invalid choice. try again.",Fore.RESET)
            if choice == '0':
                # play the game
                args.interactive = True
            elif choice == '1':
                # run benchmark
                args.benchmark = True
        if args.interactive:
            # run interactive game
            pass
        elif args.benchmark:
            benchmark = Benchmark(args)
            benchmark()
    except KeyboardInterrupt:
        print(Fore.LIGHTYELLOW_EX, "\nExiting.", Fore.RESET)
        exit(0)


if __name__ == '__main__':
    run()
