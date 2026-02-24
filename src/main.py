import sys

from db import TaskDatabase
from management import TaskManagement
from cli import TaskCli

if __name__ == "__main__":
    db = TaskDatabase()
    manager = TaskManagement(db)
    cli = TaskCli()
    
    if len(sys.argv) < 2 or sys.argv[1] == "help":
        print("Usage:")
        print("|  add <name> <description>: (optional)")
        print("|  list")
        print("|  done <id>")
        print("|  delete <id>")
        sys.exit(1)

    if sys.argv[1] == "add":
        if len(sys.argv) < 3:
            print("Error: provide a task name.")
            sys.exit(1)

        name = sys.argv[2]
        description = sys.argv[3] if len(sys.argv) > 3 else ""        
        manager.create_task(name, description)
        print("Status: task added.")
    
    elif sys.argv[1] == "list":
        cli.print_tasks(manager.show_tasks())
    
    elif sys.argv[1] == "done":
        task_id = int(sys.argv[2])

        if manager.done(task_id):
            print("Status: the task is marked as done.")
        else:
            print(f"Error: the task ({task_id}) was not found")

    elif sys.argv[1] == "del":
        task_id = int(sys.argv[2])

        if manager.delete_task(task_id):
            print("Status: the task is deleted...")
        else:
            print(f"Error: the task ({task_id}) was not found")
