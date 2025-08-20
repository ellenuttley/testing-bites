from lib.secret_diary import *
from unittest.mock import Mock
import pytest

class FakeDiary:
    def __init__(self):
        self.contents = 'this is the contents'
    
    def read(self):
        return self.contents

def test_secret_diary_functional():
    fake_diary = FakeDiary()
    secret_diary = SecretDiary(fake_diary)
    assert(secret_diary)

def test_secret_diary_sets_locked_to_true():
    fake_diary = FakeDiary()
    secret_diary = SecretDiary(fake_diary)
    assert(secret_diary.locked == True)

def test_secret_diary_read_throws_error_if_locked():
    fake_diary = FakeDiary()
    secret_diary = SecretDiary(fake_diary)

    with pytest.raises(Exception) as err:
        secret_diary.read()
    error_message = str(err.value)
    assert error_message == "Go away!"

def test_secret_diary_unlock_unlocks_diary():
    fake_diary = FakeDiary()
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    assert secret_diary.locked == False

def test_secret_diary_read_successful_if_unlocked():
    fake_diary = FakeDiary()
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'this is the contents'

def test_secret_diary_lock_locks_diary():
    fake_diary = FakeDiary()
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    secret_diary.lock()
    assert secret_diary.locked == True
