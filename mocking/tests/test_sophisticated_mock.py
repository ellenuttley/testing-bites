from unittest.mock import Mock

class FakeTaskList:
    def __init__(self):
        self.task_list = []
    
    def add(self, task):
        self.task_list.append(task)
    
    def count(self):
        return len(self.task_list)
    
    def clear(self):
        return 'success'
    
    def list(self):
        return self.task_list


def test_creates_a_sophisticated_mock():
    # Uncomment and set up your mocks here
    task_list = FakeTaskList()
    task = Mock()

    # Don't edit below
    task_list.add(task)
    assert task_list.list() == [task]
    assert task_list.count() == 1
    assert task_list.clear() == "success"
