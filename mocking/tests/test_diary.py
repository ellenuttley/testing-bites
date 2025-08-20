from lib.diary import *
import pytest

def test_diary_functional():
    diary = Diary('this is the contents')
    assert(diary)

def test_diary_read_returns_content():
    diary = Diary('this is the contents')
    assert diary.read() == 'this is the contents'
    
def test_diary_throws_error_if_none_contents():
    with pytest.raises(Exception) as err:
        Diary(None)
    error_message = str(err.value)
    assert error_message == 'This diary needs contents!'

