from lib.task_tracker import *
import pytest

def test_task_tracker_functional():
    task_tracker = TaskTracker()
    assert(task_tracker)

def test_task_tracker_add_valid_todo():
    task_tracker = TaskTracker()
    task_tracker.add('do this thing')
    assert 'do this thing' in task_tracker.todo_list

def test_task_tracker_remove_valid_todo():
    task_tracker = TaskTracker()
    task_tracker.add('do this thing')
    task_tracker.remove('do this thing')
    assert 'do this thing' not in task_tracker.todo_list

def test_task_tracker_remove_throws_error_todo_not_in_list():
    task_tracker = TaskTracker()
    with pytest.raises(Exception) as err:
        task_tracker.remove('do this thing')
    error_message = str(err.value)
    assert error_message == 'Todo not in list'

def test_task_tracker_list_todos_returns_list():
    task_tracker = TaskTracker()
    assert type(task_tracker.list_todos()) == list

def test_task_tracker_list_todos_returns_accurate_list():
    task_tracker = TaskTracker()
    task_tracker.add('do this thing')
    task_tracker.add('do that thing')
    assert task_tracker.list_todos() == ['do this thing', 'do that thing']