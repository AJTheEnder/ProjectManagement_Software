from __future__ import print_function
from datetime import date, datetime, timedelta
# Import Classes for linking the DB to the program
from Class.project import Project
from Class.task import Task
from Class.user import User
from Class.subtask import Subtask
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
                self.cursor = self.connection.cursor(buffered=True)
                
            #fill user list    
                self.cursor.execute("SELECT nom FROM Administrateur")
                name_administrateur = self.cursor.fetchall()
                #print("Administrateur", name_administrateur)
                
                self.cursor.execute("SELECT nom FROM Employe")
                name_employe = self.cursor.fetchall()
                #print("Employé", name_employe)

                self.cursor.execute("SELECT nom FROM GestionnaireDeProjet")
                name_gestionnaire = self.cursor.fetchall()
                #print("Gestionnaire de projet", name_gestionnaire)

                for x in range(len(name_administrateur)) :
                    collect_user_admin = User(name_administrateur[x][0], None, 2)
                    self.userList.append(collect_user_admin)
                for y in range(len(name_employe)) :
                    collect_user_employe = User(name_employe[y][0], None, 0)
                    self.userList.append(collect_user_employe)
                for z in range(len(name_gestionnaire)) :
                    collect_user_gestionnaire = User(name_gestionnaire[z][0], None, 1)
                    self.userList.append(collect_user_gestionnaire)

                '''for i in range(len(self.userList)) :
                    print(self.userList[i].name)'''

            #fill project   
                self.cursor.execute("SELECT nom,Temps,DateCreation,ID FROM Projet")
                name_projet = self.cursor.fetchall()               
                for x in range(len(name_projet)):
                    projet_name = Project(name_projet[x][0], name_projet[x][1], name_projet[x][2])
                    self.projectList.append(projet_name)
                    #fill project tasks list
                    self.cursor.execute("SELECT nom,Temps,Status,Etat,ID FROM Tache WHERE ProjetID = ('%s')"%name_projet[x][3])
                    TaskIDFromProjectID = self.cursor.fetchall()
                    for y in range(len(TaskIDFromProjectID)):
                        TaskFromProject = Task(TaskIDFromProjectID[y][0], TaskIDFromProjectID[y][1], TaskIDFromProjectID[y][2], TaskIDFromProjectID[y][3])
                        projet_name.tasks.append(TaskFromProject)
                        #fill Tasks subtasks list 
                        self.cursor.execute("SELECT nom,Temps,Status,Etat FROM SousTache WHERE TacheID = ('%s')"%TaskIDFromProjectID[y][4])
                        SubTaskIDFromTask = self.cursor.fetchall()
                        for z in range(len(SubTaskIDFromTask)):
                            SubTaskFromProject = Subtask(SubTaskIDFromTask[z][0], SubTaskIDFromTask[z][1], SubTaskIDFromTask[z][2], SubTaskIDFromTask[z][3])  
                            projet_name.tasks[y].subtasks.append(SubTaskFromProject)                                     

                '''for x in range(len(self.projectList)) :
                    print("\n",self.projectList[x].name,"\n")
                    for y in range(len(self.projectList[x].tasks)):
                        print("\n   ",self.projectList[x].tasks[y].name,"\n")
                        for z in range(len(self.projectList[x].tasks[y].subtasks)):
                            print("\n   ",self.projectList[x].tasks[y].subtasks[z].name,"\n")'''

                #fill Tasks employee list              
                self.cursor.execute ("SELECT ID,nom,ProjetID FROM Tache")
                TacheID = self.cursor.fetchall()
                self.cursor.execute ("SELECT TachesID,EmployeID FROM EmployeTaches")
                LinkID = self.cursor.fetchall()
                for x in range((len(TacheID))):
                    self.cursor.execute ("SELECT nom FROM Projet WHERE ID = ('%s')"%TacheID[x][2])
                    ProjetParent = self.cursor.fetchone()
                    result_Projet = self.find_Project(ProjetParent[0])
                    for y in range ((len(LinkID))):
                        if(LinkID[y][0] == TacheID[x][0]):
                            self.cursor.execute("SELECT nom FROM Employe WHERE ID =('%s')"%LinkID[y][1])
                            EmployeFromTask = self.cursor.fetchall()
                            for z in range((len(EmployeFromTask))):
                                result_User = self.find_User(EmployeFromTask[z][0])
                                result_Task = self.find_Task(TacheID[x][1],self.currentProject)
                                self.currentTask.employees.append(self.currentUser)

                '''for x in range(len(self.projectList)):
                    print("\n",self.projectList[x].name,"\n")
                    for y in range(len(self.projectList[x].tasks)):
                        print("\n   ",self.projectList[x].tasks[y].name,"\n")
                        for z in range(len(self.projectList[x].tasks[y].employees)):
                            print("\n     ",self.projectList[x].tasks[y].employees[z].name,"\n")'''
                
                #fill user project
                self.cursor.execute("SELECT nom,ID FROM GestionnaireDeProjet")
                Gestio = self.cursor.fetchall()
                for x in range ((len(Gestio))):
                    self.cursor.execute("SELECT nom FROM Projet WHERE GestionnaireID = ('%s')"%Gestio[x][1])
                    ProjectFromGestionnaire = self.cursor.fetchall()
                    for y in range ((len(ProjectFromGestionnaire))):
                        result_User = self.find_User(Gestio[x][0])
                        result_proj = self.find_Project(ProjectFromGestionnaire[y][0])                        
                        self.currentUser.projects.append(self.currentProject)

                '''for x in range(len(self.userList)):
                    print("\n",self.userList[x].name,"\n")
                    for y in range(len(self.userList[x].projects)):
                        print("\n   ",self.userList[x].projects[y].name,"\n")'''

                #fill user task
                self.cursor.execute("SELECT nom,ID FROM Employe")
                emp = self.cursor.fetchall()
                print('emp:',emp)
                self.cursor.execute ("SELECT TachesID,EmployeID FROM EmployeTaches")
                LinkID2 = self.cursor.fetchall()
                print('link:',LinkID2)
                for x in range(len(emp)):
                    for y in range(len(LinkID2)):
                        if(LinkID2[y][1] == emp[x][1]):
                            self.cursor.execute("SELECT nom, ProjetID FROM Tache WHERE ID =('%s')"%LinkID2[y][0])
                            TaskFromEmploye = self.cursor.fetchall()
                            print('taskfromemploye:',TaskFromEmploye)
                            for z in range(len(TaskFromEmploye)):
                                self.cursor.execute("SELECT nom FROM Projet WHERE ID =('%s')"%TaskFromEmploye[z][1])
                                project_Parent = self.cursor.fetchone()
                                self.cursor.execute("SELECT nom FROM Employe WHERE ID =('%s')"%LinkID2[y][1])
                                user_Parent = self.cursor.fetchone()
                                project_Result = self.find_Project(project_Parent[0])
                                task_Result = self.find_Task(TaskFromEmploye[z][0], self.currentProject)
                                user_Result = self.find_User(user_Parent[0])
                                self.currentUser.tasks.append(self.currentTask)
                
                for x in range(len(self.userList)):
                    print("\n",self.userList[x].name,"\n")
                    for y in range(len(self.userList[x].tasks)):
                        print("\n   ",self.userList[x].tasks[y].name,"\n")

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

    '''
    ||---------------------------------------------||
    ||                ADD FUNCTIONS                ||
    ||---------------------------------------------||
    '''
    
    ########################## ADD USER ##########################
    def add_User(self, name, password, status):

        user_Data = (name)
        
        if(status == '0') :
            add_User = '''INSERT INTO Employe 
                       (nom) 
                       VALUES ('%s')'''%user_Data
            self.cursor.execute("SET FOREIGN_KEY_CHECKS=0")
            self.cursor.execute(add_User)
            self.cursor.execute("SET FOREIGN_KEY_CHECKS=1")
            self.connection.commit()
        # Make sure data is committed to the database
        if(status == '1') :
            add_User = '''INSERT INTO GestionnaireDeProjet 
                       (nom) 
                       VALUES ('%s')'''%user_Data
            self.cursor.execute("SET FOREIGN_KEY_CHECKS=0")
            self.cursor.execute(add_User)
            self.cursor.execute("SET FOREIGN_KEY_CHECKS=1")
            self.connection.commit()
            # Make sure data is committed to the database
        if(status == '2') :
            add_User = '''INSERT INTO Administrateur 
                       (nom) 
                       VALUES ('%s')'''%user_Data
            self.cursor.execute("SET FOREIGN_KEY_CHECKS=0")
            self.cursor.execute(add_User)
            self.cursor.execute("SET FOREIGN_KEY_CHECKS=1")
            self.connection.commit()
            # Make sure data is committed to the database

        new_user = User(name, password, status)
        self.userList.append(new_user) 
        
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
    def add_Task(self, name, time, status, state, parent, parentID):

        task_Data = (name, time, status, state, int(parentID))

        add_Task = '''INSERT INTO Tache  
                   (nom, Temps, Status, Etat, ProjetID) 
                   VALUES ('%s', '%s', '%s', '%s', %s)'''%task_Data

        new_task = Task(name, time, status, state)
        self.currentProject.tasks.append(new_task)

        self.cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        self.cursor.execute(add_Task) #, name, time, status, state
        self.cursor.execute("SET FOREIGN_KEY_CHECKS=1")

        self.connection.commit()
        
    '''
    ||---------------------------------------------||
    ||           FIND IN LIST FUNCTIONS            ||
    ||---------------------------------------------||
    '''
        
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
    
    '''
    ||---------------------------------------------||
    ||               LINK FUNCTIONS                ||
    ||---------------------------------------------||
    '''
    
    ################## LINK EMPLOYEEPROJECT ####################
    def link_Employee_Project(self, employee, project) :
        employee_data = (employee.name)
        project_data = (project.name)
        
        # Query to register the id of the demanded elements
        select_Employee = '''SELECT id FROM Employe
                          WHERE (nom) = ('%s')'''%employee_data
        select_Project = '''SELECT id FROM Projet
                         WHERE (nom) = ('%s')'''%project_data
                         
        self.cursor.execute(select_Employee)
        employee_Result = self.cursor.fetchone()
        self.cursor.execute(select_Project)
        project_Result = self.cursor.fetchone()
        
        result = (employee_Result[0], project_Result[0])
        
        # Query to make the connection in the intermediate table
        update_Employee_Foreign_Key = '''INSERT INTO EmployeProjet
                                         (EmployeID, ProjetID)
                                         VALUES (%s, %s)'''%result
        
        self.cursor.execute(update_Employee_Foreign_Key)
        self.connection.commit()
        
    #################### LINK EMPLOYEETASK #####################
    def link_Employee_Task(self, employee, task) :
        employee_data = (employee.name)
        task_data = (task.name)
        
        # Query to register the id of the demanded elements
        select_Employee = '''SELECT id FROM Employe
                          WHERE (nom) = ('%s')'''%employee_data
        select_Task = '''SELECT id FROM Tache
                         WHERE (nom) = ('%s')'''%task_data
                         
        self.cursor.execute(select_Employee)
        employee_Result = self.cursor.fetchone()
        self.cursor.execute(select_Task)
        task_Result = self.cursor.fetchone()
        
        result = (employee_Result[0], task_Result[0])
        
        # Query to make the connection in the intermediate table
        update_Employee_Foreign_Key = '''INSERT INTO EmployeTaches
                                         (EmployeID, TachesID)
                                         VALUES (%s, %s)'''%result
        
        self.cursor.execute(update_Employee_Foreign_Key)
        self.connection.commit()
        
        employee.tasks.append(task)
        task.employee.append(employee)

    ################ LINK PROJECTPROJECTOWNER ##################
    def link_Project_ProjectOwner(self, project, projectowner) :
        projectowner_data = (projectowner.name)
        project_data = (project.name)
        
        ## Query to register the id of the demanded elements
        select_Projectowner = '''SELECT id FROM GestionnaireDeProjet
                              WHERE (nom) = ('%s')'''%projectowner_data
                         
        self.cursor.execute(select_Projectowner)
        projectowner_Result = self.cursor.fetchone()
        
        result = (projectowner_Result[0])
        
        # Query to make the connection in the intermediate table
        update_Projectowner_Foreign_Key = '''UPDATE Tache SET (ProjetID) = (%s) WHERE (nom) = (%s)'''
        input_data = (projectowner_Result, project_data)
        
        self.cursor.execute(update_Projectowner_Foreign_Key, input_data)
        self.connection.commit()
        
        projectowner.projects.append(project)
    
    #################### LINK TASKPROJECT #####################
    def link_Task_Project(self, project, task) :
        task_data = (task.name)
        project_data = (project.name)
        
        ## Query to register the id of the demanded elements
        select_Project = '''SELECT id FROM Projet
                         WHERE (nom) = ('%s')'''%project_data
                         
        self.cursor.execute(select_Project)
        project_Result = self.cursor.fetchone()
        
        result = (project_Result[0])
        
        # Query to make the connection in the intermediate table
        update_Project_Foreign_Key = '''UPDATE Tache SET (ProjetID) = (%s) WHERE (nom) = (%s)'''
        input_data = (project_Result, task_data)
        
        self.cursor.execute(update_Project_Foreign_Key, input_data)
        self.connection.commit()
        
        project.tasks.append(task)
        
    #################### LINK TASKSUBTASK ####################
    def link_Task_Subtask(self, task, subtask) :
        task_data = (task.name)
        subtask_data = (subtask.name)
        
        ## Query to register the id of the demanded elements
        select_Task = '''SELECT id FROM Tache
                         WHERE (nom) = ('%s')'''%task_data
                         
        self.cursor.execute(select_Task)
        task_Result = self.cursor.fetchone()
        
        result = (task_Result[0])
        
        # Query to make the connection in the intermediate table
        update_Task_Foreign_Key = '''UPDATE SousTache SET (TacheID) = (%s) WHERE (nom) = (%s)'''
        input_data = (task_Result, subtask_data)
        
        self.cursor.execute(update_Task_Foreign_Key, input_data)
        self.connection.commit()
        
        task.substasks.append(subtask)