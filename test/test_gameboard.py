import model.gameboard


gb = model.gameboard.Gameboard()


def test_init():
    assert isinstance(gb.number_of_colors, int)
    assert gb.number_of_colors != 0
    assert isinstance(gb.pattern_size, int)
    assert gb.pattern_size != 0
    assert isinstance(gb.attempts, int)
    assert gb.attempts != 0
    assert isinstance(gb.colors, list)
    assert len(gb.colors) == gb.number_of_colors
    assert len(gb.evaluation) == 0
    assert isinstance(gb.evaluation, list)
    assert len(gb.guessed) == 0
    assert isinstance(gb.guessed, list)
    assert len(gb.pattern) == 0
    assert isinstance(gb.pattern, list)


def test_generate_pattern():
    gb.pattern_size = 6
    gb.generate_pattern()
    assert gb.pattern is not None
    assert isinstance(gb.pattern, list)
    assert len(gb.pattern) == gb.pattern_size
    gb.pattern_size = 5
    gb.generate_pattern()
    assert gb.pattern is not None
    assert isinstance(gb.pattern, list)
    assert len(gb.pattern) == gb.pattern_size
