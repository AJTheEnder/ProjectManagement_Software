from PySide6 import QtCore, QtWidgets, QtGui
import sys

# The controller class from the MVC model
class Controller :
    # Constructor of the class
    def __init__(self, model, app) :
        self.model = model
        self.view = []
        self.app = app
            
    # This function starts the program (start the model and show the initial widget of the program)
    def start(self) :
        errorStatus = self.model.Start()
        print(errorStatus)
        if(errorStatus) :
            # If the model didn't connect to the DB show the error page.
            # self.view.show_Connection_Error_Page()
            self.view.show_Connection_Page()
        else :
            # label = QtWidgets.QLabel("Hello World", alignment=QtWidgets.AlignCenter)
            # label.show()
            self.view[0].resize(800, 600)
            self.view[0].show()
            sys.exit(self.app.exec())
            
    # This function is called whenether the view has to be change or refresh. It changes the current 
    # widget of the program.
    def refresh(self, view_Type) :
        if(view_Type == 0) :
            self.view.current_View = 0
            self.view.show_Connection_Error_Page()
        elif(view_Type == 1) :
            self.view.current_View = 1
            self.view.show_Connection_Page()
        elif(view_Type == 2) :
            self.view.current_View = 2
            self.view.show_Account_Creation_Page()
        elif(view_Type == 3) :
            self.view.current_View = 3
            self.view.show_Projects_Page()
        elif(view_Type == 4) :
            self.view.current_View = 4
            self.view.show_Gantt_Project_Page()
        elif(view_Type == 5) :
            self.view.current_View = 5
            self.view.show_Tasks_Page()
        elif(view_Type == 6) :
            self.view.current_View = 6
            self.view.show_Subtasks_Page()
        elif(view_Type == 7) :
            self.view.current_View = 7
            self.view.show_Create_Project_Page()
        elif(view_Type == 8) :
            self.view.current_View = 8
            self.view.show_Account_Page()
        elif(view_Type == 9) :
            self.view.current_View = 9
            self.view.Test()
            
    # Make the connection between the controller and the view
    def add_View(self, view) :
        self.view.append(view)
        
    def ask_For_Add_User(self, username, password, status) :
        self.model.add_User(username, password, status)
        self.refresh(1)
        
    def ask_For_Add_Project(self, project_Name, project_Time) :
        self.model.add_Project(project_Name, project_Time) 
        
    def ask_For_Add_Task(self, task_Name, task_Time, task_Status, task_State, parent, parentID):
        result = self.model.find_Project(parent)
        if(result == 0) :
            print('\n   The TASK parent is not valid, try again \n')
        else :
            self.model.add_Task(task_Name, task_Time, task_Status, task_State, parent, parentID)
        
    def ask_For_Get_All_Users(self) :
        return self.model.userList 
    
    def ask_For_Get_All_Projects_And_Tasks(self) :
        return self.model.projectList  
    
    def ask_For_Link_Employee_And_Project(self, employee_Name, project_Name) :
        result_Employee = self.model.find_User(employee_Name)
        result_Project = self.model.find_Project(project_Name)
        if(result_Employee == 0 or result_Project == 0) :
            print('\nThe PROJECT name or the USER name are not valid, try again\n')
        else :
            self.model.link_Employee_Project(self.model.currentUser, self.model.currentProject)
    
    def ask_For_Link_Employee_And_Task(self, employee_Name, task_Name) :
        result_Employee = self.model.find_User(employee_Name)
        result_Task = self.model.find_Task(task_Name)
        if(result_Employee == 0 or result_Task == 0) :
            print('\nThe TASK name or the USER name are not valid, try again\n')
        else :
            self.model.link_Employee_Task(self.model.currentUser, self.model.currentTask)
            
    def ask_For_Link_Projectowner_And_Project(self, project_Name, projectowner_Name) :
        result_Project = self.model.find_Project(project_Name)
        result_Projectowner = self.model.find_User(projectowner_Name)
        if(result_Project == 0 or result_Projectowner == 0) :
            print('\nThe PROJECT name or the PROJECT OWNER name are not valid, try again\n')
        else :
            self.model.link_Project_Projectowner(self.model.currentProject, self.model.currentUser)

    def ask_For_Link_Project_And_Task(self, project_Name, task_Name) :
        result_Project = self.model.find_Project(project_Name)
        result_Task = self.model.find_Task(task_Name)
        if(result_Project == 0 or result_Task == 0) :
            print('\nThe PROJECT name or the TASK name are not valid, try again\n')
        else :
            self.model.link_Task_Project(self.model.currentProject, self.model.currentTask)
            
    def ask_For_Link_Task_And_Subtask(self, task_Name, subtask_Name) :
        result_Task = self.model.find_Task(task_Name)
        current_Task = self.model.currentTask
        result_Subtask = self.model.find_Task(subtask_Name)
        current_Subtask = self.model.currentTask
        if(result_Subtask == 0 or result_Task == 0) :
            print('\nThe TASK name or the SUBTASK name are not valid, try again\n')
        else :
            self.model.link_Task_Project(current_Task, current_Subtask)