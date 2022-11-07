import PySide6.QtWidgets
import mysql.connector
from mysql.connector import Error

class Project:
    def __init__(self, id, name, time, date):
        self.id = id
        self.name = name
        self.time = time
        self.date = date
