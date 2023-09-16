# (c) 2018 Manikandan

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return f'Username: {self.username}\nTasks:\n{"".join([str(task) + "//n" for task in self.tasks])}'
