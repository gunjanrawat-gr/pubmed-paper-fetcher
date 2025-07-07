from get_papers import filters

def test_is_non_academic():
    assert filters.is_non_academic("Pfizer Inc.") is True
    assert filters.is_non_academic("Harvard University") is False
