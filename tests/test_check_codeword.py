from lib.check_codeword import *

def test_codeword_horse():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

def test_codeword_almost_horse():
    result = check_codeword('house')
    assert result == "Close, but nope."

def test_codeword_almost_horse_needs_both_letters():
    result = check_codeword('hutch')
    result2 = check_codeword('mouse')
    assert result and result2 == "WRONG!"

def test_codeword_not_horse():
    result = check_codeword('goat')
    assert result == "WRONG!"

def test_codeword_very_not_horse():
    result = check_codeword('7')
    assert result == "WRONG!"
