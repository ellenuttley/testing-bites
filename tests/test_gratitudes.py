from lib.gratitudes import *

def test_gratitudes_init_empty_list():
    test_gratitudes = Gratitudes()
    assert test_gratitudes.gratitudes == []

def test_gratitudes_add():
    test_gratitudes = Gratitudes()
    test_gratitudes.gratitudes.append('good thing')
    assert test_gratitudes.gratitudes == ['good thing']

def test_gratitudes_format():
    test_gratitudes = Gratitudes()
    test_gratitudes.gratitudes.append('good thing')
    assert test_gratitudes.format() == "Be grateful for: good thing"

def test_gratitudes_format_multiple():
    test_gratitudes = Gratitudes()
    test_gratitudes.gratitudes.append('good thing')
    test_gratitudes.gratitudes.append('and another')
    assert test_gratitudes.format() == "Be grateful for: good thing, and another"

# def test_gratitudes_():
#     pass

# def test_gratitudes_():
#     pass