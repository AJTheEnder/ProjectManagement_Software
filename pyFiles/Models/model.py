# Import Classes for linking the DB to the program
#import Class.project
#import Class.task
#import Class.user

# Import SQL module for Controlling DB
import mysql.connector
from mysql.connector import Error

# The model class from the MVC model 
class Model :
    # Constructor of the class
    def __init__(self) :
        # Model variables list in order to contain DB datas
        self.userList = []
        self.projectList = []
        self.taskListFromProject = []
        self.subtaskListFromTask = []

        # Model variables for current status of the program
        self.currentUser = 0
        self.currentProject = 0
        self.currentTask = 0

        # State of the DB connection
        self.connection = 0
        self.cursor = 0

    # This function is called at the begining of the program in order to link all datas from DB to the program
    def Start(self) :
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                 database='Electronics',
                                                 user='pynative',
                                                 password='pynative@#29')
            if self.connection.is_connected() :
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                print("You're connected to database: ", record)
                return False

        except Error as e :
            print("Error while connecting to MySQL", e)
            return True

    # This function is called at the end of the program in order to resolve all datas from DB to the program 
    def Close(self) :
        if self.connection.is_connected() :
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")