from lib.password_checker import *
import pytest

def test_password_checker_init():
    password_checker = PasswordChecker()
    assert password_checker

def test_password_checker_valid_password():
    password_checker = PasswordChecker()
    assert password_checker.check('password') == True

def test_password_checker_invalid_password():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as err:
        password_checker.check('pass')
    error_message = str(err.value)
    assert error_message == "Invalid password, must be 8+ characters."