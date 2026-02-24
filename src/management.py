from model import Task
from db import TaskDatabase

class TaskManagement:
    """
    Creates the class to do the managment
    """
    def __init__(self, database: TaskDatabase):
        self.db = database
        self.tasks = self.db.load()
        
    """
    Creates the task with a id autoincremented
    Params: name(str)
    """
    def create_task(self, name: str, description: str = ""):
        id = max([t.id for t in self.tasks], default=0) + 1
        task = Task(id, name, description, False)
        self.tasks.append(task)
        self.db.save(self.tasks)

    def delete_task(self, task_id: int):
        for t in self.tasks:
            if t.id == task_id:
                self.tasks.remove(t)
                self.db.save(self.tasks)
                return True
        
        return False

    def show_tasks(self):
        return self.tasks
    
    def done(self, task_id: int):
        for t in self.tasks:
            if t.id == task_id:
                t.completed = True
                self.db.save(self.tasks)

                return True

        return False
