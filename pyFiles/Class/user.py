import PySide6.QtWidgets
import mysql.connector
from mysql.connector import Error

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
