from lib.present import *
import pytest

def test_present_init():
    test_present = Present()
    assert test_present

def test_present_wrap():
    test_present = Present()
    test_present.wrap('book')
    assert test_present.contents == 'book'

def test_present_wrap_already_a_present():
    test_present = Present()
    test_present.wrap('book')
    with pytest.raises(Exception) as err:
        test_present.wrap('teddy')
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."

def test_present_unwrap():
    test_present = Present()
    test_present.wrap('book')
    assert test_present.unwrap() == 'book'

def test_present_unwrap_no_present():
    test_present = Present()
    with pytest.raises(Exception) as err:
        test_present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."
