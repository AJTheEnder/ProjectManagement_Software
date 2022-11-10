import PySide6.QtWidgets
import mysql.connector
from mysql.connector import Error

class Task:
    def __init__(self, name, time, status, state, subtasks):
        self.id = id
        self.name = name
        self.time = time
        self.status = status
        self.state = state
        self.subtasks = subtasks


