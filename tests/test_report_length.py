from lib.report_length import *

def test_report_length_accurate():
    result = report_length('hello')
    assert '5' in result

def test_report_length_format():
    result = report_length('hello')
    assert result == "This string was 5 characters long."

def test_report_length_short_string():
    result = report_length('h')
    assert result == "This string was 1 characters long."

def test_report_length_long_string():
    result = report_length('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    assert result == "This string was 100 characters long."

def test_report_length_no_string():
    result = report_length('')
    assert result == "This string was 0 characters long."