from controller.controller_unit import Controller
from colorama import Fore, init as fore_init
from arg_parser import init_parser
fore_init()

parser = init_parser()

game = Controller("brute_force", parser, attempts=1000)
game()

print(Fore.LIGHTBLUE_EX, "Welcome to the game Logik!", Fore.RESET)
print("This implementation was created by Michal Polovka in 2017.\n"
      "Shareable under GPL-3.0 licence.\n"
      "See the game repository for details: https://github.com/miskopo/Logiks")
print()
if parser.args.interactive is None and parser.args.benchmark is None:
    print(Fore.LIGHTBLUE_EX,"You didn't choose whether you want to play or to run benchmark", Fore.RESET)

