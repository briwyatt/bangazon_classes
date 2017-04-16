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

    methods: __init__, payroll
    '''
    def __init__(self, name, payroll)
        super().__init__()
        self.name = name
        self.payroll = list()

    def payroll(self, payroll):
        ''' Lists the names of employees responsible for payroll
       
        Arguments:
        payroll - string
        '''
        return self.payroll


class Sales(Department):
    ''' Sales is a subclass of the Department class
    
    Arguments:
    
    
     '''
    def __init__(self, name, goals, history)


