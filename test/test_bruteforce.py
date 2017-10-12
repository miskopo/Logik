from controller.brute_force import BruteForce

bruteforce = BruteForce(colors=[range(8)], pattern_size=5 )


def test_init():
    assert len(bruteforce.colors) == 8
    assert bruteforce.pattern_size == 5


def guess_pattern():
    pass
