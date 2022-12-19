# Import Classes for the view to recognize DB datas
import Class.project
import Class.task
import Class.user

# The view class from the MVC model
class View :
    # Constructor of the class
    def __init__(self, controller) :
        self.current_View = 0
        self.controller = controller
        
        
        
    '''
    ||---------------------------------------------||
    ||                 ERROR PAGE                  ||
    ||---------------------------------------------||
    '''
    
    # This page occures when the connection to the DB has fail and shows an error message
    def show_Connection_Error_Page(self) :
        print('\nERROR TO CONNECTION DATABASE, PLEASE MAKE SURE TO HAVE AN INTERNET CONNECTION\n')
        
        
        
    '''
    ||---------------------------------------------||
    ||               CONNECTION PAGE               ||
    ||---------------------------------------------||
    '''
    
    def show_Connection_Page (self) :
        username = input('\n\nEnter your username : \n') 
        if (self.controller.ask_For_Find_User(username) != 0):
            self.controller.make_User_In_Use()
            self.controller.refresh(1)
        else:
            self.controller.refresh(4)
            
            

    '''
    ||---------------------------------------------||
    ||                  MENU PAGE                  ||
    ||---------------------------------------------||
    '''
     
    def show_Menu_Page(self) :
        valid_Choice = False
        while(valid_Choice == False) :
            print('\nMENU PAGE\n'
                  '\n[1] -- Add an user (Admin only)\n'
                  '\n[2] -- Add a project with tasks (Admin and Project owner only)\n'
                  '\n[3] -- Show all users (Admin Only)\n'
                  '\n[4] -- Show all projects and tasks informations of a user\n'
                  '\n[5] -- Link an employee to a task (Admin and Project owner only)\n'
                  '\n[6] -- Add a task to an existing project (Admin and Project owner only)\n'
                  '\n[7] -- Link a product owner to a project (Admin only)\n'
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
                self.controller.refresh(10)
                valid_Choice = True
            elif(choice == '6') :
                self.controller.refresh(11)
                valid_Choice = True
            elif(choice == '7') :
                self.controller.refresh(13)
                valid_Choice = True
            else :
                print('\nINVALID CHOICE\n')
                
                
    
    '''
    ||---------------------------------------------||
    ||              CREATE USER PAGE               ||
    ||---------------------------------------------||
    '''
       
    def show_Account_Creation_Page(self) :
        current_User = self.controller.ask_For_Get_User_In_Use()
        if (current_User.status == 2 ) :
            print('\nACCOUNT CREATION PAGE\n')
            username = input('\nEnter a USERNAME : \n')
            password = input('\nEnter a PASSWORD : \n')
            status = input('\nEnter your STATUS (Employee : [0] / Project owner : [1] / Admin : [2]) : \n')
            while(status != '0' and status != '1' and status != '2') :
                print('\nWRONG ANSWER\n')
                status = input('\nEnter your STATUS (Employee : [0] / Project owner : [1] / Admin : [2]) : \n')
            self.controller.ask_For_Add_User(username, password, status)  
        else:
            print("\nYou don't have permission to do this, please make sure you are an admin")
            self.controller.refresh(1) 
            
             
            
    '''
    ||---------------------------------------------||
    ||             CREATE PROJECT PAGE             ||
    ||---------------------------------------------||
    '''
    
    def show_Create_Project_Page(self) :
        current_User = self.controller.ask_For_Get_User_In_Use()
        if (current_User.status == 1 or current_User.status == 2 ) :
            print('\nPROJECT CREATION PAGE\n')
            project_Name = input('\nEnter a PROJECT NAME : \n')
            project_Time = input('\nEnter the TOTAL TIME of the project : \n')
            choice = input('\nDo you want to create a task for this project ? [YES] / [NO]\n')
            parent_ID = self.controller.ask_For_Add_Project(project_Name, project_Time)
            if (current_User.status == 1) :
                self.controller.ask_For_Link_Projectowner_And_Project(project_Name, current_User.name)
            while(choice == 'YES') :
                task_Name = input('\n   Enter the TASK NAME : \n')
                task_Time = input('\n   Enter the TOTAL TIME of the task : \n')
                task_Status = input('\n   Enter the TASK STATUS : [BACKLOG] / [IN PROGRESS] / [READY] / [IN REVIEW] / [DONE] : \n')
                task_State = input('\n   Enter the TASK STATE : [OPEN] / [CLOSE]) : \n')
                self.controller.ask_For_Add_Task(task_Name, task_Time, task_Status, task_State, project_Name, parent_ID)
                choice = input('\nDo you want to create a task for this project ? [YES] / [NO]\n')
            self.controller.refresh(1)
        else:
            print("\nYou don't have permission to do this, please make sure you are a product owner")
            self.controller.refresh(1)
            
            
            
    '''
    ||---------------------------------------------||
    ||              SHOW ALL USER PAGE             ||
    ||---------------------------------------------||
    '''

    def show_Account_Page(self) :
        print('\nACCOUNT PAGE\n')
        current_User = self.controller.ask_For_Get_User_In_Use()
        if (current_User.status == 2) :
            users_List = self.controller.ask_For_Get_All_Users()
            for i in range(len(users_List)) :
                print('\n\nUser NAME : ', users_List[i].name)
                print('\nUser PASSWORD : ', users_List[i].password)
                print('\nUser STATUS : ', users_List[i].status)
            end = input('\n\nPress [ENTER] to go back to MENU...\n')
            self.controller.refresh(1)
        else:
            print("\nYou don't have permission to do this, please make sure you are an admin")
            self.controller.refresh(1)
            
            

    '''
    ||---------------------------------------------||
    ||       SHOW PROJECTS INFORMATIONS PAGE       ||
    ||---------------------------------------------||
    '''
   
    def show_Projects_Page(self) :
        print('\nPROJECTS PAGE\n')
        current_User = self.controller.ask_For_Get_User_In_Use()
        if (current_User.status == 2 ) :
            projects_List = self.controller.ask_For_Get_All_Project_Informations_For_A_User()
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

        elif (current_User.status == 1 ):
            projects_List = self.controller.ask_For_Get_All_Project_Informations_For_A_User()
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

        elif (current_User.status == 0 ):
            tasks_List = self.controller.ask_For_Get_All_Project_Informations_For_A_User()
            for i in range(len(tasks_List)) :
                print('\nTask NAME : ', tasks_List[i].name)
                print('\nTask TIME : ', tasks_List[i].time)
                print('\nTask STATUS : ', tasks_List[i].status)
                print('\nTask STATE : ', tasks_List[i].state, '\n')
            end = input('\n\nPress ENTER to go back to MENU\n')     
        self.controller.refresh(1)
        
        

    '''
    ||---------------------------------------------||
    ||            LINK EMPLOYEE TO TASK            ||
    ||---------------------------------------------||
    '''
    
    def link_Employee_Task(self) :
        current_User = self.controller.ask_For_Get_User_In_Use()
        if (current_User.status == 1 or current_User.status == 2) :
            users_List = self.controller.ask_For_Get_All_Users()
            print ('\nEMPLOYEE REGISTERED : \n')
            for i in range(len(users_List)) :
                if(users_List[i].status == 0) :
                    print(users_List[i].name)

            print ('\nTASK YOU OWNED : \n')
            if (current_User.status == 1) :
                for i in range(len(current_User.projects)) :
                    for j in range(len(current_User.projects[i].tasks)) :
                        print((current_User.projects[i].tasks[j].name))
            else :
                project_List = self.controller.ask_For_Get_All_Projects_And_Tasks()
                for i in range(len(project_List)) :
                    for j in range(len(project_List[i].tasks)) :
                        print(project_List[i].tasks[j].name)
    
            employee_Name = input('\nEnter an employee NAME to link a task to : \n')
            task_Name = input('\nEnter a task NAME to link : \n')
            self.controller.ask_For_Link_Employee_And_Task(employee_Name, task_Name)
            self.controller.refresh(1)
        else :
            print("\nYou don't have permission to do this, please make sure you are an admin or a project owner")
            self.controller.refresh(1)
            
            

    '''
    ||---------------------------------------------||
    ||             ADD TASK TO PROJECT             ||
    ||---------------------------------------------||
    '''
    
    def add_Task_Project(self) :
        current_User = self.controller.ask_For_Get_User_In_Use()
        if (current_User.status == 1 or current_User.status == 2 ) :
            project_List = self.controller.ask_For_Get_All_Projects_And_Tasks()
            print ('\nPROJECT YOU OWNED : \n')
            if(current_User.status == 2) :
                for i in range(len(project_List)) :
                    print(project_List[i].name)
            else :
                for i in range(len(current_User.projects)) :
                    print(current_User.projects[i].name)

            project_Name = input('\nEnter a project NAME to link a task to : \n')
            self.controller.ask_For_Find_Project(project_Name)
            parent_ID = self.controller.ask_For_Find_Project_ID(project_Name)
            task_Name = input('\n   Enter the TASK NAME : \n')
            task_Time = input('\n   Enter the TOTAL TIME of the task : \n')
            task_Status = input('\n   Enter the TASK STATUS : [BACKLOG] / [IN PROGRESS] / [READY] / [IN REVIEW] / [DONE] : \n')
            task_State = input('\n   Enter the TASK STATE : [OPEN] / [CLOSE]) : \n')
            self.controller.ask_For_Add_Task(task_Name, task_Time, task_Status, task_State, project_Name, parent_ID)
            self.controller.refresh(1)
        else:
            print("\nYou don't have permission to do this, please make sure you are a product owner")
            self.controller.refresh(1)
            
            

    '''
    ||---------------------------------------------||
    ||             LINK PO TO PROJECT              ||
    ||---------------------------------------------||
    '''
    
    def link_ProductOwner_Project(self) :
        current_User = self.controller.ask_For_Get_User_In_Use()
        productOwner_List = self.controller.ask_For_Get_All_Users()
        if (current_User.status == 2) :
            print ('\nPRODUCT OWNER REGISTERED : \n')
            for i in range(len(productOwner_List)) :
                if (productOwner_List[i].status == 1) :
                    print( productOwner_List[i].name)

            project_List = self.controller.ask_For_Get_All_Projects_And_Tasks()
            print ('\nEXISTING PROJECT : \n')
            for i in range(len(project_List)) :
                print(project_List[i].name)

            employee_Name = input('\nEnter a project owner NAME to link to a project : \n')
            project_Name = input('\nEnter a project NAME to link : \n')
            self.controller.ask_For_Link_Projectowner_And_Project(project_Name, employee_Name)
            self.controller.refresh(1)
        else:
            print("\nYou don't have permission to do this, please make sure you are a product owner")
            self.controller.refresh(1)
