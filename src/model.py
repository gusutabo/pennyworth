class Task:
    """
    Creates the structure that contains the task atributes
    Params: id(int), name(str), description(str), completed(boolean)
    """
    def __init__(self, id: int, 
                 name: str, description: str, 
                 completed: bool):
        self.id = id
        self.name = name
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data: dict):
        return Task(
            data["id"],
            data["name"],
            data["description"],
            data["completed"]
        )
    