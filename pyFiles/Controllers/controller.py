# The controller class from the MVC model
class Controller :
    # Constructor of the class
    def __init__(self, model) :
        self.model = model
        self.view = 0
            
    # This function starts the program (start the model and show the initial widget of the program)
    def start(self) :
        errorStatus = self.model.Start()
        if(errorStatus) :
            # If the model didn't connect to the DB show the error page.
            # self.view.show_Connection_Error_Page()
            self.view.show_Connection_Page()
        else :
            # If the model did connect to the DB show the connection page.
            self.view.show_Connection_Page()
            
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
            
    # Make the connection between the controller and the view
    def add_View(self, view) :
        self.view = view
        
    def ask_For_Add_User(self, username, password) :
        self.model.add_User(username, password)
        self.refresh(1)
        
    def ask_For_Add_Project(self, project_Name, project_Time) :
        self.model.add_Project(project_Name, project_Time) 
        
    def ask_For_Add_Task(self, task_Name, task_Time, task_Status, task_State, parent):
        result = self.model.find_Project(parent)
        if(result == 0) :
            print('\n   The TASK parent is not valid, try again \n')
        else :
            self.model.add_Task(task_Name, task_Time, task_Status, task_State, parent)
        
    def ask_For_Get_All_Users(self) :
        return self.model.userList 
    
    def ask_For_Get_All_Projects_And_Tasks(self) :
        return self.model.projectList  