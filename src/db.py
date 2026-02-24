import json
import os

from model import Task

class TaskDatabase:
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save(self, tasks: list):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

    def load(self):
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as file:
            data = json.load(file)
            return [Task.from_dict(item) for item in data]
        