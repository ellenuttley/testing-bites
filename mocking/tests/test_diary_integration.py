from lib.diary import *
from lib.secret_diary import *
import pytest

'''
Create the diary, and try to read it. 
Because it is unlocked, should get "Go Away"
'''
def test_secret_diary_raises_error_when_locked():
    diary = Diary('This is the diary contents')
    secret_diary = SecretDiary(diary)
    
    with pytest.raises(Exception) as err:
        secret_diary.read()
    error_message = str(err.value)
    assert error_message == "Go away!"


'''
Create a diary, unlock it, and read it
'''
def test_secret_diary_read_diary_when_unlocked():
    diary = Diary('This is the diary contents')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    print(secret_diary.locked, secret_diary.diary.contents)
    assert secret_diary.read() == 'This is the diary contents'

'''
Create a diary, unlock it
Then lock it again, and try to read - should throw error
'''
def test_secret_diary_no_read_diary_when_relocked():
    diary = Diary('This is the diary contents')
    secret_diary = SecretDiary(diary)

    secret_diary.unlock()
    secret_diary.lock()

    with pytest.raises(Exception) as err:
        secret_diary.read()
    error_message = str(err.value)
    assert error_message == "Go away!"