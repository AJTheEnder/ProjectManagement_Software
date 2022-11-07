import PySide6.QtWidgets
import mysql.connector
from mysql.connector import Error

class Task:
    def __init__(self, id, name, time, status, state):
        self.id = id
        self.name = name
        self.time = time
        self.status = status
        self.state = state
