# (c) 2018 Manikandan

class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        return f'Title: {self.title}\nDescription: {self.description}\nStatus: {"Completed" if self.completed else "Incomplete"}'
