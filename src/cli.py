class TaskCli:
    """
    Handles the CLI display logic 
    for showing tasks to the user
    """
    def print_tasks(self, tasks: list):
        """
        Prints the list of tasks in a formatted way

        Parameters:
            tasks (list): List of Task objects to display.
        """
        if not tasks:
            print("No tasks available")
            return None
        
        for task in tasks:
            status = "x" if task.completed else " "
            print(f"[{status}] {task.id} -> {task.name} {task.description}")    
            