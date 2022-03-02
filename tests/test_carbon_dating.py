from carbon_dating import get_age_carbon_14_dating

def test_get_age_carbon_14_dating():
    assert round(get_age_carbon_14_dating(0.35), 2) == 8680.35

def test_get_age_carbon_14_dating_zero():
    assert get_age_carbon_14_dating(0) == "Error: Carbon-14 ration must be between 0 and 1."

def test_get_age_carbon_14_dating_negative():
    assert get_age_carbon_14_dating(-0.1) == "Error: Carbon-14 ration must be between 0 and 1."