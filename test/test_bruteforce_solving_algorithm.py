from controller.brute_force_solving_algorithm import BruteForce

brute_force = BruteForce(colors=range(8), pattern_size=5, attempts=12)


def test_init():
    assert len(brute_force.colors) == 8
    assert brute_force.pattern_size == 5


def test_guess_pattern():
    brute_force.guess_pattern()
    assert len(brute_force.guessed) != 0
    assert isinstance(brute_force.guessed, list)
    assert isinstance(brute_force.guessed[0], list)
