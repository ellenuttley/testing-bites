from lib.greet import *

def test_correct_name():
    result = greet('Greg')
    assert result == "Hello, Greg!"