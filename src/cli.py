from colors import Colors

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
            print(Colors.RED + "Error: no tasks available" + Colors.RESET)
            return None
        
        print(Colors.BLUE + "*) Tasks:" + Colors.RESET)
        for task in tasks:
            status = "x" if task.completed else " "
            print(f"[{status}] {task.id} -> {task.name} {task.description}")    