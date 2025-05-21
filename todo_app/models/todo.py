class Todo:
    todos_list = []
    next_id = 1

    def __init__(self, title, description=None):
        self.id = Todo.next_id
        Todo.next_id += 1
        self.title = title
        self.description = description
        self.completed = False

    def __repr__(self):
        return f"<Todo {self.id}: {self.title}>"
