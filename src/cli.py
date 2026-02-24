class TaskCli:
    def print_tasks(self, tasks: list):
        if not tasks:
            print("No task disponivel")
            return None
        
        for task in tasks:
            status = "x" if task.completed else " "
            print(f"[{status}] {task.id} -> {task.name} {task.description}")    
            