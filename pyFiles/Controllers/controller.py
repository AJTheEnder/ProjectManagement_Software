# The controller class from the MVC model
class Controller :
    # Constructor of the class
    def __init__(self, model) :
        self.model = model
        self.view = []
        # self.app = app
            
    # This function starts the program (start the model and show the initial widget of the program)
    def start(self) :

        
        errorStatus = self.model.Start()
        if(errorStatus) :
            # self.view[0].resize(800, 600)
            # self.view[0].show()
            # self.view[0].show_Connection_Error_Page()
            # sys.exit(self.app.exec())

            # If the model didn't connect to the DB show the error page.
            self.refresh(0)
        else :
            self.refresh(4)
            
    # This function is called whenether the view has to be change or refresh. It changes the current 
    # widget of the program.
    def refresh(self, view_Type) :
        if(view_Type == 0) :
            self.view[0].current_View = 0
            self.view[0].show_Connection_Error_Page()
        elif(view_Type == 1) :
            self.view[0].current_View = 1
            self.view[0].show_Menu_Page()
        elif(view_Type == 2) :
            self.view[0].current_View = 2
            self.view[0].show_Account_Creation_Page()
        elif(view_Type == 3) :
            self.view[0].current_View = 3
            self.view[0].show_Projects_Page()
        elif(view_Type == 4) :
            self.view[0].current_View = 4
            self.view[0].show_Connection_Page()
        elif(view_Type == 5) :
            self.view[0].current_View = 5
            self.view[0].show_Tasks_Page()
        elif(view_Type == 6) :
            self.view[0].current_View = 6
            self.view[0].show_Subtasks_Page()
        elif(view_Type == 7) :
            self.view[0].current_View = 7
            self.view[0].show_Create_Project_Page()
        elif(view_Type == 8) :
            self.view[0].current_View = 8
            self.view[0].show_Account_Page()
        elif(view_Type == 9) :
            self.view[0].current_View = 9
            self.view[0].link_Employee_Project()
        elif(view_Type == 10) :
            self.view[0].current_View = 10
            self.view[0].link_Employee_Task()
        elif(view_Type == 11) :
            self.view[0].current_View = 11
            self.view[0].add_Task_Project()
        elif(view_Type == 12) :
            self.view[0].current_View = 12
            self.view[0].link_Task_Subtask()
        elif(view_Type == 13) :
            self.view[0].current_View = 13
            self.view[0].link_ProductOwner_Project()

            
    # Make the connection between the controller and the view
    def add_View(self, view) :
        self.view.append(view)
        
    def ask_For_Add_User(self, username, password, status) :
        self.model.add_User(username, password, status)
        self.refresh(1)
        
    def ask_For_Add_Project(self, project_Name, project_Time) :
        self.model.add_Project(project_Name, project_Time)
        return self.model.find_ID_Project(project_Name) 
        
    def ask_For_Add_Task(self, task_Name, task_Time, task_Status, task_State, parent, parentID):
        result = self.model.find_Project(parent)
        if(result == 0) :
            print('\n   The TASK parent is not valid, try again \n')
        else :
            self.model.add_Task(task_Name, task_Time, task_Status, task_State, parentID)
        
    def ask_For_Get_All_Users(self) :
        return self.model.userList 
    
    def ask_For_Get_All_Projects_And_Tasks(self) :
        return self.model.projectList  

    def ask_For_Get_All_Tasks_And_Subtasks(self) :
        task_List = []
        for i in range(len(self.model.projectList)) :
            for j in range(len(self.model.projectList[i].tasks)) :
                task_List.append(self.model.projectList[i].tasks[j])
        return task_List
 
    
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
            self.model.link_Project_ProjectOwner(self.model.currentProject, self.model.currentUser)

    def ask_For_Link_Project_And_Task(self, project_Name, task_Name) :
        result_Project = self.model.find_Project(project_Name)
        result_Task = self.model.find_Task(task_Name, result_Project)
        if(result_Project == 0 or result_Task == 0) :
            print('\nThe PROJECT name or the TASK name are not valid, try again\n')
        else :
            print('\nThe PROJECT name and the TASK succeded link\n')
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


    def ask_For_Get_All_Project_Informations_For_A_User(self) :
        return self.model.get_All_User_Project_Informations()

    def ask_For_Get_User_In_Use(self) :
        return self.model.userInUse 

    def ask_For_Find_User(self, username):
        return  self.model.find_User(username)

    def make_User_In_Use(self):
        self.model.userInUse = self.model.currentUser
        
    def ask_For_Find_Project_ID(self, project_Name) :
        return self.model.find_ID_Project(project_Name)
    
    def ask_For_Find_Project(self, project_Name) :
        result_Project = self.model.find_Project(project_Name)
        if(result_Project == 0) :
            print('\nThe PROJECT name or the PROJECT OWNER name are not valid, try again\n')
            self.refresh(1)