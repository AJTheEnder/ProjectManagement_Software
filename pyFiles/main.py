# Imports MVC files
import Controllers.controller as c
import Models.model as m
import Views.view as v

# Initialising the MVC model
model = m.Model()
controller = c.Controller(model)
view = v.View(controller)
controller.AddView(view)
controller.Start()