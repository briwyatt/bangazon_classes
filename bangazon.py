# Create a Department class. Create some simple properties and methods on Department. 
# You are going to create some derived classes that inherit from Department, 
# so make sure that the properties/methods you add are general to all Departments.

class Department(object):

    def __init__(self, name, supervisor, location, employee_count):
        self.name = name
        self.supervisor = supervisor
        self.location = location
        self.employee_count = employee_count
        self.budget = 100000
    def get_dept_name(self):
        return self.name

    def count_employees(self):
        return self.employee_count

    def find_department(self):
        return self.location

    def find_supervisor(self):
        return self.supervisor

     
    def get_employees(self):
        return self.employees

    def add_employees(self, employee):
        self.employees.append(employee) 

    def meet(self):
        return "Meet in the conference room for an important presentation."

    def get_budget(self):
        return self.budget


class Sales(Department):

    def __init__(self, name, supervisor, location, employee_count):
        super().__init__(name, supervisor,location, employee_count)
        self.awards = ()
        self.budget = super().get_budget() - 7000
        self.employees = [self.supervisor]  


    def add_awards(self, award_name, award_year):

        self.awards.add("Dundie Award", "2006")


class Customer_Service(Department):

    def __init__(self, name, supervisor, location, employee_count):
        super().__init__(name, supervisor,location, employee_count)
        self.refund_policies = list()
        self.budget = super().get_budget() + -2000
        self.employees = [self.supervisor]  

    def add_policies(self, policy_name, policy_content):
        self.refund_policies.append(("No Refunds for Golden Ticket items"))

class Accounting(Department):

    def __init__(self, name, supervisor, location, employee_count):
        super().__init__(name, supervisor,location, employee_count)
        self.employees = [self.supervisor]  

        self.budget = super().get_budget() -2500

class Human_Resources(Department):

    def __init__(self, name, supervisor, location, employee_count):
        super().__init__(name, supervisor,location, employee_count)
        self.computers = ()
        self.employees = [self.supervisor]  


        self.budget = super().get_budget() -3000

    def add_computer_equipment(self, computer_type):

        self.add_computer_equipment(computer_type)


if __name__ == '__main__':
    # main()

    sales = Sales("Sales", "Dwight Schrute", "Middle of the Room", 4)
    customer_service = Customer_Service("Customer Service", "Kelly Kapoor", "The Appendix", 1)
    accounting = Accounting("Accounting", "Oscar Martinez", "Left Corner", 10)
    HR = Human_Resources("Human Resources", "Toby Flenderson", "The Appendix", 1)

    print(sales.name)
    print(customer_service.name)
    print(accounting.name)
    print(HR.name)

    sales.add_employees ("Pam Beesly")
    sales.add_employees("Jim Halpert")
    sales.add_employees("Andy Bernard")
    print(sales.get_employees())

    print(customer_service.get_employees())

    accounting.add_employees("Angela Martin")
    accounting.add_employees("Kevin Malone")
    print(accounting.get_employees())

    HR.add_employees("Holly Flax")
    print(HR.get_employees())

    print("sales budget = ", sales.budget)
    print("customer_service budget = ", customer_service.budget)
    print("accounting budget = ", accounting.budget)
    print("HR budget = ", HR.budget)








