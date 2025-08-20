import pytest
from unittest.mock import Mock

# Delete the lines starting with `@pytest.mark.skip` one by one as you work through.
class FakeObject:
    def speak(self, name):
        return f"Meow, {name}"
    
    def count_ears(self):
        return 2

    def count_legs(self):
        return 4

def test_set_up_blank_mock():
    fake_object = FakeObject()

    # Don't edit below
    assert fake_object is not None


def test_set_up_mock_with_methods():
    fake_object = FakeObject()

    # Don't edit below
    assert fake_object.speak("Jess") == "Meow, Jess"
    assert fake_object.count_ears() == 2
    assert fake_object.count_legs() == 4

def test_assert_that_mock_was_called():
    fake_object = Mock()

    # Don't edit this next line
    fake_object.speak("Steve")
    fake_object.speak.return_value = "Steve"

    # Write an assertion below that the method "speak" was called with
    # the argument "Steve"
    assert fake_object.speak() == "Steve"

def test_creates_mock_for_specific_case():
    fake_diary = Mock()

    # Set up this mock to pass the tests below
    # ...
    
    fake_diary.count_entries.return_value = 2
    
    # Don't edit below
    fake_diary.add(Mock())
    fake_diary.add(Mock())
    assert fake_diary.count_entries() == 2

