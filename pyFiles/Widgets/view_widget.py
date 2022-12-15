import Class.project
import Class.task
import Class.user

# Import necessaries for PyQT
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):

    def __init__(self, controller):
        super().__init__()

        # widget = QtWidgets.QWidget()
        # layout = QtGui.QWidget(widget)
        # widget.setLayout(layout)

        self.controller = controller

        self.profil_Button = QtWidgets.QPushButton("Profil")
        self.profil_Button.setMinimumWidth(150)

        self.text = QtWidgets.QLabel("Hello World",
                                    alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.profil_Button)

        self.profil_Button.clicked.connect(print("toto"))

    # @QtCore.Slot()

                # This page shows the informations of the current user.
    def show_Account_Page(self) :

        # self.layout = QtWidgets.QVBoxLayout(self)
        # self.layout.addWidget(self.text)

        self.text = QtWidgets.QLabel("Profil Page",
                            alignment=QtCore.Qt.AlignTop)

        self.text.show()

        users_List = self.controller.ask_For_Get_All_Users()
        for i in range(len(users_List)) :

            self.text = QtWidgets.QLabel("User Name : ", users_List[i].name,
                     alignment=QtCore.Qt.AlignLeft)

            print('\n\nUser NAME : ', users_List[i].name)
            print('\nUser PASSWORD ', users_List[i].password)
        end = input('\n\nPress ENTER to go back to MENU\n')
        self.controller.refresh(1)

    def show_Connection_Error_Page(self) :

        # self.layout = QtWidgets.QVBoxLayout(self)
        self.text = QtWidgets.QLabel("Error to connection of database, \n Please make sure to have an internet connection",
                            alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)

        self.text.resize(300, 100)
        self.text.show()

        self.connection_page_Button = QtWidgets.QPushButton("Return")
        self.connection_page_Button.setMinimumWidth(150)

        # self.layout.addWidget(self.connection_page_Button)

        self.connection_page_Button.clicked.connect(self.show_Connection_Page)
    
        self.connection_page_Button.show()



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
                  '\n6 -- link an project to a task\n'
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
            elif(choice == '6') :
                self.controller.refresh(10)
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
            task_ParentID = input('\n   Enter the parentID : \n')
            self.controller.ask_For_Add_Task(task_Name, task_Time, task_Status, task_State, project_Name, task_ParentID)
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

    def Test(self) :
        print('\nALL LINK TESTS\n')

        employee_Name = input('\nEnter an employee NAME to link a project to : \n')
        project_Name = input('\nEnter a project NAME to link : \n')
        self.controller.ask_For_Link_Employee_And_Project(employee_Name, project_Name)

        employee_Name = input('\nEnter an employee NAME to link a task to : \n')
        task_Name = input('\nEnter a task NAME to link : \n')
        self.controller.ask_For_Link_Employee_And_Task(employee_Name, task_Name)

        employee_Name = input('\nEnter a project owner NAME to link to a project : \n')
        project_Name = input('\nEnter a project NAME to link : \n')
        self.controller.ask_For_Link_Projectowner_And_Project(project_Name, employee_Name)

        project_Name = input('\nEnter a project NAME to link a task to : \n')
        task_Name = input('\nEnter a task NAME to link : \n')
        self.controller.ask_For_Link_Project_And_Task(project_Name, task_Name)

        #task_Name = input('\nEnter a task NAME to link a subtask to: \n')
        #subtask_Name = input('\nEnter a subtask NAME to link : \n')
