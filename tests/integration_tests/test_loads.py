from server import load_clubs, load_competitions


def test_load_json_functions():
    clubs = load_clubs()
    assert clubs is not None
    assert isinstance(clubs, list)
    assert len(clubs) > 0

    competitions = load_competitions()
    assert competitions is not None
    assert isinstance(competitions, list)
    assert len(competitions) > 0
