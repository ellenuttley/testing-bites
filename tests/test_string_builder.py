from lib.string_builder import *

def test_string_builder_init():
    test_string = StringBuilder()
    assert test_string

def test_string_builder_add():
    test_string = StringBuilder()
    test_string.add('h')
    assert test_string.str == 'h'

def test_string_builder_size():
    test_string = StringBuilder()
    test_string.add('h')
    assert test_string.size() == 1

def test_string_builder_size_multiple_adds():
    test_string = StringBuilder()
    test_string.add('h')
    test_string.add('e')
    assert test_string.size() == 2

def test_string_builder_size_empty_string():
    test_string = StringBuilder()
    test_string.add('')
    assert test_string.size() == 0

def test_string_builder_output():
    test_string = StringBuilder()
    test_string.add('hello')
    assert test_string.output() == 'hello'

def test_string_builder_output_empty_string():
    test_string = StringBuilder()
    test_string.add('')
    assert test_string.output() == ''