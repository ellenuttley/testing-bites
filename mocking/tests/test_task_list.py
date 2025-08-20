from lib.task_list import TaskList
from unittest.mock import Mock

def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []

def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

def test_task_list_add_appends_task():
    task_list = TaskList()
    mock_task = Mock('task')
    task_list.add(mock_task)
    assert mock_task in task_list.tasks

def test_task_list_all_returns_all_tasks():
    task_list = TaskList()
    mock_task = Mock('task')
    mock_task_2 = Mock('task2')
    task_list.add(mock_task)
    task_list.add(mock_task_2)
    assert len(task_list.all()) == 2

def test_task_list_all_compete_true_all_complete():
    task_list = TaskList()
    mock_complete = FakeCompletedTask()

    task_list.add(mock_complete)

    assert task_list.all_complete() == True

def test_task_list_all_compete_false_not_all_complete():
    task_list = TaskList()
    mock_complete = FakeCompletedTask()
    mock_not_complete = FakeNotCompletedTask()

    task_list.add(mock_complete)
    task_list.add(mock_not_complete)

    assert task_list.all_complete() == False

class FakeCompletedTask():
    def is_complete(self):
        return True

class FakeNotCompletedTask():
    def is_complete(self):
        return False

# Unit test `#tasks` and `#all_complete` behaviour
