import PySide6.QtWidgets
import mysql.connector
from mysql.connector import Error

class User:
	def __init__(self, name, password):
		self.name = name	
		self.password = password

	