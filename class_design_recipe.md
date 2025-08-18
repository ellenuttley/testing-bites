# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TaskTracker():
    init:
    todo_list = list, for ongoing to-dos

def add_todo(todo)
# add a todo to the list with append

def delete_todo(todo)
# delete a todo from the list with remove

def list_todos()
# returns the list
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a valid todo
#add adds the to-do to the list
"""
task_tracker = TaskTracker()
task_tracker.add('do this thing')
assert 'do this thing' in task_tracker.todo_list

"""
Given a valid todo
#remove removes the to-do to the list
"""
task_tracker = TaskTracker()
task_tracker.add('do this thing')
task_tracker.remove('do this thing')
assert 'do this thing' not in task_tracker.todo_list

"""
Given a todo that isn't in the list
#remove throws an exception
"""
task_tracker = TaskTracker()
assert task_tracker.remove('do this thing') throws exception

"""
#list_todos returns a list
"""
task_tracker = TaskTracker()
assert task_tracker.list_todos() returns list

"""
given valid todos
#list_todos returns a list containing the todos
"""
task_tracker = TaskTracker()
task_tracker.add('do this thing')
task_tracker.add('do that thing')
assert task_tracker.list_todos() == ['do this thing', 'do that thing']
"""

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
