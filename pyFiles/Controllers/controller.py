# The controller class from the MVC model
class Controller :
    # Constructor of the class
    def __init__(self, model) :
        self.model = model
        self.view = 0
            
    # This function starts the program (start the model and show the initial widget of the program)
    def Start(self) :
        errorStatus = self.model.Start()
        if(errorStatus) :
            # If the model didn't connect to the DB show the error page.
            self.view.ShowConnectionErrorPage()
        else :
            # If the model did connect to the DB show the connection page.
            self.view.ShowConnectionPage()
            
    # This function is called whenether the view has to be change or refresh. It changes the current 
    # widget of the program.
    def Refresh(self, viewType) :
        if(viewType == 0) :
            self.view.currentView = 0
            self.view.ShowConnectionErrorPage()
        elif(viewType == 1) :
            self.view.currentView = 1
            self.view.ShowConnectionPage()
        elif(viewType == 2) :
            self.view.currentView = 2
            self.view.ShowAccountCreationPage()
        elif(viewType == 3) :
            self.view.currentView = 3
            self.view.ShowProjectsPage()
        elif(viewType == 4) :
            self.view.currentView = 4
            self.view.ShowGanttProjectPage()
        elif(viewType == 5) :
            self.view.currentView = 5
            self.view.ShowTasksPage()
        elif(viewType == 6) :
            self.view.currentView = 6
            self.view.ShowSubtasksPage()
            
    # Make the connection between the controller and the view
    def AddView(self, view) :
        self.view = view