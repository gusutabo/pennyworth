class Task:
    """
    Represents the task structure
    
    Attributes: 
            id: int, 
            name: str, 
            description: str, 
            completed: boolean
    """
    def __init__(self, id: int, 
                 name: str, description: str, 
                 completed: bool):
        self.id = id
        self.name = name
        self.description = description
        self.completed = completed

    def to_dict(self):
        """
        Converts the Task object into a dictionary.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Creates a Task object from a dictionary.
        
        Parameters:
            data (dict): Dictionary containing the keys
                         'id', 'name', 'description' and 'completed'.
        """
        return Task(
            data["id"],
            data["name"],
            data["description"],
            data["completed"]
        )
    