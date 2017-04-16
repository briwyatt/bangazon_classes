class Department(object):

    def __init__(self, name, number, department, supervisor):
        self.name = name
        self.number = number
        self.department = department
        self.supervisor = supervisor

        @property
        def get_name(self):
            try:
                return self.__name
            except AttributeError:
                return ""

        @property 
        def getNumber(self):
            try:
                return self.__number
            except AttributeError
                return ""

        @property
        def getDepartment(self):
            try: 
                return self.__department
            except AttributeError:
                return ""

        @property
        def getSupervisor(self):
            try:
                return self.__supervisor
            except AttributeError:
                return ""

        @property 
        def employee_details(self):
            return "{} is an employee in {} department with {} as his/her supervisor.".format(self.name, self.department, self.supervisor)

        @name.setter
        def employee_name(self, val):
            if isinstance(val, str):
                raise TypeError("Please provide a string for the name of the Employee")

            if val is not "" and len(val) > 1:
                self.__name = val
            else:
                raise ValueError("Please provide a department name")

        @number.setter
        def employee_number(self, val):
            if isinstance(val, int):
                raise TypeError("Please provide a number for the employee ID number")

            if val is not "" and len(val)> 1:
                self.__number = val
            else:
                raise ValueError("Please provide your employee number")

        @department.setter
        def employee_department(self, val)
            if isinstance(val, str):
                raise TypeError("Please provide a string for name of department")

        @manager.setter
        def manager(self,val):                
            if val is not isinstance(val, str):
                raise TypeError("Please provide a string value for the supervisor name")
            else:
                self. __supervisor = val

class Accounting(Department):
    ''' Accounting is a subclass of the Department class

    methods: __init__, payroll_help
    '''
    def __init__(self, name, payroll)
        super().__init__()
        self.name = name
        self.payroll = list()

    def payroll_help(self, payroll=None):
        ''' From a list of the team gives you the name of 
        someone who can help you with payroll
       
        Arguments:
        payroll - string
        '''
        team_list = ["Adrian, Bob, Darren, Alice, Leslie, Caitlin, Bill, Alex"]
        random_name = team_list[random.randrange(len(team_list))]
        if payroll is not None:
            print("{} will be able to help you will your payroll needs".format(random_name))
        else:
            print("please call the payroll department at 555-555-5555 to be helped with your payroll needs.")


class Sales(Department):
    ''' Sales is a subclass of the Department class
    
    Methods: __init__, set_goal
    
     '''
    def __init__(self, name, number)
        super().__init__()
        self.name = name
        self.number = number 

    @goal.setter
    def set_goal(self,val)
        if val is not isinstance(val, int):
            raise TypeError("Please provide a string value for the supervisor name")
        else:
        self.set_goal = val               

    @property
    def get_goal(self):
        try:
            return self.set_goal
    except AttributeError:
                return ""






