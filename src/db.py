import json
import os

from model import Task

class TaskDatabase:
    """
    Handles task persistence using a .json file
    Saving and loading tasks from disk
    """
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save(self, tasks: list):
        """
        Saves a list of Task objects to a .json file
        
        Parameters: 
            tasks (list): list of the objects to be saved
        """
        
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

    def load(self):
        """
        Loads tasks from the .json file
        
        Returns: 
            list: a list of task objects. If the file does not exists
                  returns an empty list.
        """
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as file:
            data = json.load(file)
            return [Task.from_dict(item) for item in data]
        