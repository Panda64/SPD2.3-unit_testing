from calculate_grades import calculate_stat

def test_calculate_grades():
    assert calculate_stat([1,2,3,4,5])[0] == 3.0
    assert round(calculate_stat([1,2,3,4,5])[1], 3) == 1.414