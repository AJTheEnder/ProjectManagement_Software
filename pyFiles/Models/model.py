from __future__ import print_function
from datetime import date, datetime, timedelta
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
            self.connection = mysql.connector.connect(host='mysql-rdefaria.alwaysdata.net',
                                         database='rdefaria_projectmanagement',
                                         user='rdefaria',
                                         password='petitdeuf1')
            
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self.cursor = self.connection.cursor()

                self.cursor.execute("SELECT nom FROM Administrateur")
                name_administrateur = self.cursor.fetchone()
                print("rdefaria_projectmanagement", name_administrateur)
                
                self.cursor.execute("SELECT nom FROM Employe")
                name_employe = self.cursor.fetchone()
                print("rdefaria_projectmanagement", name_employe)

                self.cursor.execute("SELECT nom FROM GestionnaireDeProjet")
                name_gestionnaire = self.cursor.fetchone()
                print("rdefaria_projectmanagement", name_gestionnaire)

                self.userList.append(name_administrateur)
                self.userList.append(name_employe)
                self.userList.append(name_gestionnaire)
                print(self.userList)
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
    def add_User(self, name, password, status):

        user_Data = (name)
        
        if(status == 0) :
            add_User = '''INSERT INTO Employe 
                       (nom) 
                       VALUES ('%s')'''%user_Data
        if(status == 1) :
            add_User = '''INSERT INTO Gestionnaire_de_projet 
                       (nom) 
                       VALUES ('%s')'''%user_Data
        if(status == 2) :
            add_User = '''INSERT INTO Administrateur 
                       (nom) 
                       VALUES ('%s')'''%user_Data

        new_user = User(name, password, status)
        self.userList.append(new_user)

        self.cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        self.cursor.execute(add_User)
        self.cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        # Make sure data is committed to the database
        self.connection.commit()
        
    ######################### ADD PROJECT #########################
    def add_Project(self, name, time):

        tomorrow = datetime.now().date()

        project_Data = (tomorrow, name, time)
        
        add_Project = '''INSERT INTO Projet  
                      (DateCreation, nom, Temps) 
                      VALUES ('%s', '%s', '%s')'''%project_Data
        
        new_project = Project(name, time, tomorrow)
        self.projectList.append(new_project)

        self.cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        self.cursor.execute(add_Project) #, name, time
        self.cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        self.connection.commit()

    ########################## ADD TASK ##########################
    def add_Task(self, name, time, status, state, parent):

        task_Data = (name, time, status, state)

        add_Task = '''INSERT INTO Tache  
                   (nom, Temps, Status, Etat) 
                   VALUES ('%s', '%s', '%s', '%s')'''%task_Data

        new_task = Task(name, time, status, state)
        self.currentProject.tasks.append(new_task)

        self.cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        self.cursor.execute(add_Task) #, name, time, status, state
        self.cursor.execute("SET FOREIGN_KEY_CHECKS=1")

        self.connection.commit()
        
    ######################### FIND USER #########################
    def find_User(self, name) :
        for i in range(len(self.userList)) :
            if(self.userList[i].name == name) :
                self.currentUser = self.userList[i]
                return self.userList[i]
        return 0
    
    ####################### FIND PROJECT ########################
    def find_Project(self, name) :
        for i in range(len(self.projectList)) :
            if(self.projectList[i].name == name) :
                self.currentProject = self.projectList[i]
                return self.projectList[i]
        return 0
    
    ######################### FIND TASK #########################
    def find_Task(self, name, project) :
        for i in range(len(project.tasks)) :
            if(project.tasks[i].name == name) :
                self.currentTask = project.tasks[i]
                return project.tasks[i]
        return 0
    
    ####################### FIND SUBTASK ########################
    def find_Subtask(self, name, task) :
        for i in range(len(task.subtasks)) :
            if(task.subtasks[i].name == name) :
                self.currentTask = task.subtask[i]
                return task.subtasks[i]
        return 0