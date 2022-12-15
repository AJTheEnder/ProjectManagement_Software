# Imports MVC files
import Controllers.controller as c
import Models.model as m
import Views.view as v
# import Widgets.view_widget as w
# from PySide6 import QtCore, QtWidgets, QtGui
# import sys


# app = QtWidgets.QApplication(sys.argv) 

# Initialising the MVC model
model = m.Model()
controller = c.Controller(model)
view = v.View(controller)

# view = w.MyWidget(controller)

controller.add_View(view)

# show_connection = w.show_connection(controller)
# controller.add_View(show_connection)

controller.start()