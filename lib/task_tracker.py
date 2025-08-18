class TaskTracker():
    def __init__(self):
        self.todo_list = []
    
    def add(self, todo):
        self.todo_list.append(todo)

    def remove(self, todo):
        if todo not in self.todo_list:
            raise Exception('Todo not in list')
        self.todo_list.remove(todo)
    
    def list_todos(self):
        return self.todo_list