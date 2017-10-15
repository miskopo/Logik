from controller.brute_force import BruteForce

bruteforce = BruteForce(colors=range(8), pattern_size=5, attempts=12)


def test_init():
    assert len(bruteforce.colors) == 8
    assert bruteforce.pattern_size == 5


def guess_pattern():
    bruteforce.guess_pattern()
    assert len(bruteforce.guessed) != 0
    assert isinstance(bruteforce.guessed, list)
    assert isinstance(bruteforce.guessed[0], list)
