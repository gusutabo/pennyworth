from model import Task
from db import TaskDatabase

class TaskManagement:
    """
    Handles the managements operations such as creating,
    deleting, listing and completing tasks.
    """
    def __init__(self, database: TaskDatabase):
        self.db = database
        self.tasks = self.db.load()
        
    def create_task(self, name: str, description: str = ""):
        """
        Creates the task with a id autoincremented
        
        Parameters: 
            name (str): name of the task
            description (str): optional task description
        """

        id = max([t.id for t in self.tasks], default=0) + 1
        task = Task(id, name, description, False)
        self.tasks.append(task)
        self.db.save(self.tasks)

    def delete_task(self, task_id: int):
        """
        Deletes a task by its Id 
        
        Parameters: 
            task_id (int): ID of the Task to be removed
        """
        for t in self.tasks:
            if t.id == task_id:
                self.tasks.remove(t)
                self.db.save(self.tasks)
                return True
        
        return False

    def show_tasks(self):
        """
        Returns all the tasks that exists in the database 
        
        Returns: 
            task (list): list of tasks objects
        """
        return self.tasks
    
    def done(self, task_id: int):
        """
        Mark a existing task as done 
        
        Parameters: 
            task_id (int): ID of the Task to mark as done
        """
        for t in self.tasks:
            if t.id == task_id:
                t.completed = True
                self.db.save(self.tasks)

                return True

        return False 
