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
        self.currentView = 0
        self.controller = controller
        
    # This page occures when the connection to the DB has fail and shows an error message
    def ShowConnectionErrorPage(self) :
        print('ERROR TO CONNECTION DATABASE')

    # This page shows a place to write a username and a password, if the connection has fail show an error message 
    # if not continue in program in function of the type of user (admin, project owner, employee)  
    # You can also decide to create a user so you go to account create page.    
    def ShowConnectionPage(self) :
        print('CONNECTION PAGE')

    # This page lets you create an account with your informations. If you are an admin you have to insert the 
    # ADMIN KEY, if you are a project owner you have to insert the PROJECT OWNER KEY.    
    def ShowAccountCreationPage(self) :
        print('ACCOUNT CREATION PAGE')

    # This page shows the projects you are owning in function of your user status. This page is inaccessible for 
    # regular employees.    
    def ShowProjectsPage(self) :
        print('PROJECTS PAGE')

    # This page shows all the tasks of a project in a Gantt form. This page is inaccessible for regular employees.
    def ShowGanttProjectPage(self) :
        print('GANTT PROJECT PAGE')

    # For admins and project owners this page shows all the tasks of a project, for an employee this page shows
    # all the tasks he is assigned of.    
    def ShowTasksPage(self) :
        print('TASKS PAGE')
    
    # This page shows all the sub-tasks of a task/subt-ask.   
    def ShowSubtasksPage(self) :
        print('SUBTASKS PAGE')