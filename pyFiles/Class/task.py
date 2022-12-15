class Task:
    def __init__(self, name, time, status, state):
        self.name = name
        self.time = time
        self.status = status
        self.state = state
        # self.ID = ID
        self.subtasks = []
        self.employees = []


