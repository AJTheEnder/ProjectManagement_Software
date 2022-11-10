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
    # You can also decide to create a user so you go to account create page.    
    def show_Connection_Page(self) :
        print('\nCONNECTION PAGE\n')
        confirmation = input('\nEnter YES to connect :\n')
        while(confirmation != 'YES') :
            confirmation = input('\nEnter YES to connect :\n')
        self.controller.refresh(7)
            

    # This page lets you create an account with your informations. If you are an admin you have to insert the 
    # ADMIN KEY, if you are a project owner you have to insert the PROJECT OWNER KEY.    
    def show_Account_Creation_Page(self) :
        print('\nACCOUNT CREATION PAGE\n')
        username = input('\nEnter a USERNAME :\n')
        self.controller.ask_For_Add_User(username)    

    # This page shows the projects you are owning in function of your user status. This page is inaccessible for 
    # regular employees.    
    def show_Projects_Page(self) :
        print('\nPROJECTS PAGE\n')

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
        
    # This page shows the informations of the current user. (Temporally the menu page)
    def show_Account_Page(self) :
        print('\nMENU PAGE\n')
        choice = input('\nCHOICE :\n')