from controller.single_color import SingleColor

single_color = SingleColor(colors=range(8), pattern_size=5, attempts=12)


def test_init():
    assert len(single_color.colors) == 8
    assert single_color.pattern_size == 5


def guess_pattern():
    single_color.guess_pattern()
    assert len(single_color.guessed) != 0
    assert isinstance(single_color.guessed, list)
    assert isinstance(single_color.guessed[0], list)
