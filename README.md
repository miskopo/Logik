# Logik :octocat:  
[![Build Status](https://travis-ci.org/miskopo/Logik.svg?branch=master)](https://travis-ci.org/miskopo/Logik)
[![codecov](https://codecov.io/gh/miskopo/Logik/branch/master/graph/badge.svg)](https://codecov.io/gh/miskopo/Logik)



Logik game implementation with various solving strategies.
This implementation servers primarily as school project.


Logik is a game known to world as **Mastermind**, however in former Czechoslovakia it was known as Logik:

_Mastermind or Master Mind is a code-breaking game for two players. The modern game with pegs was invented in 1970 by Mordecai Meirowitz, an Israeli postmaster and telecommunications expert. It resembles an earlier pencil and paper game called Bulls and Cows that may date back a century or more._ 
[Wikipedia](https://en.wikipedia.org/wiki/Mastermind_(board_game))


## Objectives:
- [x] Implement game engine and grading system
- [ ] Implement solving strategies
- [ ] Run automated games and collect data about overall efficiency and plot them.

## Solving strategies:
- [x] **Brute force**: computer tries every possibility till it finds solution or loose, eventually
- [x] **Single color**: computer always fills answering row with single color up to point it knows all used colors, then switches to brute force
- [ ] **Semi-random**: computer fills random colors and remembers correct colors/positions. This is human-like approach.
- [x] **True random**: computer fills random colors forever. Or till it wins, which is unlikely, to be honest.
