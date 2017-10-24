from controller.true_random_solving_algorithm import TrueRandom

true_random = TrueRandom(colors=range(8), pattern_size=5, attempts=12)


def test_init():
    assert len(true_random.colors) == 8
    assert true_random.pattern_size == 5


def guess_pattern():
    true_random.guess_pattern()
    assert len(true_random.guessed) != 0
    assert isinstance(true_random.guessed, list)
    assert isinstance(true_random.guessed[0], list)

