import model.gameboard


gb = model.gameboard.Gameboard()


def test_init():
    assert len(gb.evaluation) == 0
    assert len(gb.guessed) == 0
    assert len(gb.pattern) == 0


def test_generate_pattern():
    gb.pattern_size = 6
    gb.generate_pattern()
    assert isinstance(gb.pattern, str)
    assert len(gb.pattern) == gb.pattern_size
    gb.pattern_size = 5
    gb.generate_pattern()
    assert isinstance(gb.pattern, str)
    assert len(gb.pattern) == gb.pattern_size