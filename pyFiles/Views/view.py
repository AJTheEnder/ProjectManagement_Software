# Import Classes for the view to recognize DB datas
import Class.project
import Class.task
import Class.user

# Import necessaries for PyQT
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

# Cette classe définit un widget pour QT (Tiré de l'exemple du tuto), il faudra l'adapté pour ensuite
# en créer une instance qui nous servira à afficher une fenêtre avec le programme avec les données du
# model. 
'''
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
'''

# The view class from the MVC model
class View :
    # Constructor of the class
    def __init__(self, controller) :
        self.current_View = 0
        self.controller = controller
        
    # This page occures when the connection to the DB has fail and shows an error message
    def show_Connection_Error_Page(self) :
        print('\nERROR TO CONNECTION DATABASE\n')

    # This page shows a place to write a username and a password, if the connection has fail show an error message 
    # if not continue in program in function of the type of user (admin, project owner, employee)  
    # You can also decide to create a user so you go to account create page. (Temporally the menu page)   
    def show_Connection_Page(self) :
        valid_Choice = False
        while(valid_Choice == False) :
            print('\nMENU PAGE\n'
                  '\n1 -- Add a user\n'
                  '\n2 -- Add a project with tasks\n'
                  '\n3 -- show all users\n'
                  '\n4 -- show all project with their tasks\n'
                  '\n5 -- link an employee to a task\n'
                  )
            choice = input('\nCHOICE : \n')
            if(choice == '1') :
                self.controller.refresh(2)
                valid_Choice = True
            elif(choice == '2') :
                self.controller.refresh(7)
                valid_Choice = True
            elif(choice == '3') :
                self.controller.refresh(8)
                valid_Choice = True
            elif(choice == '4') :
                self.controller.refresh(3)
                valid_Choice = True
            elif(choice == '5') :
                self.controller.refresh(9)
                valid_Choice = True
            else :
                print('\nINVALID CHOICE\n')
            

    # This page lets you create an account with your informations. If you are an admin you have to insert the 
    # ADMIN KEY, if you are a project owner you have to insert the PROJECT OWNER KEY.    
    def show_Account_Creation_Page(self) :
        print('\nACCOUNT CREATION PAGE\n')
        username = input('\nEnter a USERNAME : \n')
        password = input('\nEnter a PASSWORD : \n')
        status = input('\nEnter your STATUS (Employee : 0 / Project owner : 1 / Admin : 2) : \n')
        while(status != '0' and status != '1' and status != '2') :
            print('\nWRONG ANSWER\n')
            status = input('\nEnter your STATUS (Employee : 0 / Project owner : 1 / Admin : 2) : \n')
        self.controller.ask_For_Add_User(username, password, status)    

    # This page shows the projects you are owning in function of your user status. This page is inaccessible for 
    # regular employees.    
    def show_Projects_Page(self) :
        print('\nPROJECTS PAGE\n')
        projects_List = self.controller.ask_For_Get_All_Projects_And_Tasks()
        for i in range(len(projects_List)) :
            print('\n\nProject NAME : ', projects_List[i].name)
            print('\nThis project takes ', projects_List[i].time, ' in total')
            print('\nTASKS of the project : \n')
            for j in range(len(projects_List[i].tasks)) :
                print('\nTask NAME : ', projects_List[i].tasks[j].name)
                print('\nTask TIME : ', projects_List[i].tasks[j].time)
                print('\nTask STATUS : ', projects_List[i].tasks[j].status)
                print('\nTask STATE : ', projects_List[i].tasks[j].state, '\n')
        end = input('\n\nPress ENTER to go back to MENU\n')
        self.controller.refresh(1)

    # This page shows all the tasks of a project in a Gantt form. This page is inaccessible for regular employees.
    def show_Gantt_Project_Page(self) :
        print('\nGANTT PROJECT PAGE\n')

    # For admins and project owners this page shows all the tasks of a project, for an employee this page shows
    # all the tasks he is assigned of.    
    def show_Tasks_Page(self) :
        print('\nTASKS PAGE\n')
    
    # This page shows all the sub-tasks of a task/subt-ask.   
    def show_Subtasks_Page(self) :
        print('\nSUBTASKS PAGE\n')
        
    # This page allow the user to create a project with tasks.
    def show_Create_Project_Page(self) :
        print('\nPROJECT CREATION PAGE\n')
        project_Name = input('\nEnter a PROJECT NAME : \n')
        project_Time = input('\nEnter the TOTAL TIME of the project : \n')
        choice = input('\nDo you want to create a task for this project ? YES/NO\n')
        self.controller.ask_For_Add_Project(project_Name, project_Time)
        while(choice == 'YES') :
            task_Name = input('\n   Enter the TASK NAME : \n')
            task_Time = input('\n   Enter the TOTAL TIME of the task : \n')
            task_Status = input('\n   Enter the TASK STATUS (BACKLOG / IN PROGRESS / READY / IN REVIEW / DONE) : \n')
            task_State = input('\n   Enter the TASK STATE (OPEN / CLOSE) : \n')
            self.controller.ask_For_Add_Task(task_Name, task_Time, task_Status, task_State, project_Name)
            choice = input('\nDo you want to create a task for this project ? YES/NO\n')
        self.controller.refresh(1)
               
    # This page shows the informations of the current user. 
    def show_Account_Page(self) :
        print('\nACCOUNT PAGE\n')
        users_List = self.controller.ask_For_Get_All_Users()
        for i in range(len(users_List)) :
            print('\n\nUser NAME : ', users_List[i].name)
            print('\nUser PASSWORD ', users_List[i].password)
        end = input('\n\nPress ENTER to go back to MENU\n')
        self.controller.refresh(1)
        
    #-----------------------#
    # TEMPORARY FOR TESTING #
    #-----------------------#
    
    def link_Employee_To_Task_Page(self) :
        print('\nLINK EMPLOYEE TO TASK PAGE\n')
        employee_Name = input('\nEnter an employee NAME to link : \n')
        task_Name = input('\nEnter a task NAME to link : \n')
        self.controller.ask_For_Link_Employee_And_Task(employee_Name, task_Name)
        self.controller.refresh(1)