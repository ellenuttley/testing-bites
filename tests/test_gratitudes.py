from lib.gratitudes import Gratitudes

def test_gratitudes_init_empty_list():
    test_gratitudes = Gratitudes()
    assert test_gratitudes.gratitudess == []

def test_gratitudes_add():
    test_gratitudes = Gratitudes()
    test_gratitudes.add('good thing')
    assert test_gratitudes.gratitudess == ['good thing']

def test_gratitudes_format():
    test_gratitudes = Gratitudes()
    test_gratitudes.add('good thing')
    assert test_gratitudes.format() == "Be grateful for: good thing"

def test_gratitudes_format_multiple():
    test_gratitudes = Gratitudes()
    test_gratitudes.add('good thing')
    test_gratitudes.add('and another')
    assert test_gratitudes.format() == "Be grateful for: good thing, and another"