from extract_position import extract_position

def test_extract_position_error():
    assert extract_position("[error] test test test") == None

def test_extract_position_debug():
    assert extract_position("[debug] test test test") == None

def test_extract_position():
    assert extract_position("|update| the positron location in the particle accelerator is x:21.432") == "21.432"