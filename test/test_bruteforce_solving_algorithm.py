from controller.brute_force_solving_algorithm import BruteForce

brute_force = BruteForce(colors=range(8), pattern_size=5, attempts=12)


def test_init():
    assert len(brute_force.colors) == 8
    assert brute_force.pattern_size == 5


def test_guess_pattern():
    brute_force.guess_pattern()
    assert isinstance(brute_force.guessed, list)
    assert isinstance(brute_force.guessed[0], list)
    assert len(brute_force.guessed) != 0
    brute_force.attempts = 100000
    brute_force.guessed = []
    brute_force.guess_pattern()
    assert len(brute_force.guessed) == len(brute_force.colors) ** brute_force.pattern_size


def test_decide_next_step():
    assert brute_force.decide_next_step([str(-1) for _ in range(brute_force.pattern_size)], brute_force.pattern_size) == 'continue'
    assert brute_force.decide_next_step(['-1','0','1','-1','1'], 5) == 'continue'
    assert brute_force.decide_next_step([str(1) for _ in range(5)], 5) == 'finish'
