# Import Classes for linking the DB to the program
from Class.project import Project
from Class.task import Task
from Class.user import User
# Import SQL module for Controlling DB
import mysql.connector
from mysql.connector import Error

# The model class from the MVC model


class Model:
    # Constructor of the class
    def __init__(self):
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
    def Start(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                      database='Electronics',
                                                      user='pynative',
                                                      password='pynative@#29')
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                print("You're connected to database: ", record)
                return False

        except Error as e:
            print("Error while connecting to MySQL", e)
            return True

    # This function is called at the end of the program in order to resolve all datas from DB to the program
    def Close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")

    ########################## ADD USER ##########################
    def add_User(self, name, password):

        add_User = ("INSERT INTO Employe " #penser a bien relier les noms de tab
                    "(name) "
                    "VALUES (%s)")

        new_user = User(self, name)
        self.userList.append(new_user)

        self.cursor.execute(add_User, name)
        # Make sure data is committed to the database
        self.connection.commit()

    ########################## ADD TASK ##########################
    def add_Task(self, name, time, status, state):

        add_Task = ("INSERT INTO Tache " #penser a bien relier les noms de tab
                    "(name, time, status, state) "
                    "VALUES (%s, %s, %s, %s)")


        new_task = Task(self, name, time, status, state)
        self.taskListFromProject.append(new_task)

        self.cursor.execute(add_Task, name, time, status, state)
        # Make sure data is committed to the database
        self.connection.commit()


    ######################### ADD PROJECT #########################
    def add_Project(self, name, time, date):

        add_Projet = ("INSERT INTO Projet " #penser a bien relier les noms de tab
                    "(name, time, status, state) "
                    "VALUES (%s, %s, %s, %s)")


        new_project = Project(self, name, time, date)
        self.projectList.append(new_project)

        self.cursor.execute(add_Task, name, time, status, state)
        # Make sure data is committed to the database
        self.connection.commit()


    
        


        




