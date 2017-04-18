# Create a Department class. Create some simple properties and methods on Department. 
# You are going to create some derived classes that inherit from Department, 
# so make sure that the properties/methods you add are general to all Departments.
import random 

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

    def meet(self):
       return "Everybody meet in {}'s office for the presentation".format(self.supervisor)

class Customer_Service(Department):

    def __init__(self, name, supervisor, location, employee_count):
        super().__init__(name, supervisor,location, employee_count)
        self.refund_policies = list()
        self.budget = super().get_budget() + -2000
        self.employees = [self.supervisor]  

    def add_policies(self, policy_name, policy_content):
        self.refund_policies.append(("No Refunds for Golden Ticket items"))

    def meet(self):
       return "Everybody meet in the co for the presentation".format(self.supervisor)
   
class Accounting(Department):

    def __init__(self, name, supervisor, location, employee_count):
        super().__init__(name, supervisor,location, employee_count)
        self.employees = [self.supervisor]  

    def meet(self):
        return "Everybody meet in {}'s desk to look at the news story about the Scranton Strangler".format(self.supervisor)

        self.budget = super().get_budget() -2500

class Human_Resources(Department):

    def __init__(self, name, supervisor, location, employee_count):
        super().__init__(name, supervisor,location, employee_count)
        self.computers = ()
        self.employees = [self.supervisor]  

        self.budget = super().get_budget() -3000

    def add_policies(self, policy):
        self.policy = policy

class Employee(object):
    def __init__(first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name

    def eat(self, food=None, companions=None):
        restaurants = ["Chili's", "Alfredo's Pizza Cafe", "Brunetti's Pizza" "Cooper's Seafood", "Hooters", "Cugino's" "Poor Richards"]
        restaurants = random.choice(restaurants)
        self.food = food
        self.companions = companions

        if food is None and companions is None:
            print("{} went out to eat at {}".format(self.full_name, self.restaurant))
            return self.restaurant
        elif food is "sandwich" and companions is None
            print("{} ate a {} in the breakroom at the office.".format(self.full_name, self.food))
        elif food is None and companions is self.companions:
            print("{} all ate at {} today".format(self.companions, self.restaurants))
        else:
            print("{} {} ate at {}".format(self.firstName, self.lastName, random_resturant))
            return random_resturant

# eat()
'''
Will select a random restaurant name from a list of strings, print to console
 that the employee is at that restaurant, and also return the restaurant.
'''

# eat(food="sandwich")
'''
Will output that the employee ate that specific food at the office.
'''

# eat(companions=[Sam, Dean, Alice])
'''
Will select a random restaurant name from a list of strings, print to console
that the employee is at that restaurant, and also output 
the first name of each employee in the specified list.
'''

# eat("pizza", [Sam, Dean, Alice])
'''
'''


if __name__ == '__main__':
    # main()

    sales = Sales("Sales", "Dwight Schrute", "Middle cubicles of the Office", 4)
    customer_service = Customer_Service("Customer Service", "Kelly Kapoor", "The Appendix", 1)
    accounting = Accounting("Accounting", "Oscar Martinez", "Left Corner cubicles", 10)
    HR = Human_Resources("Human Resources", "Toby Flenderson", "The Appendix", 1)

    print(sales.name)
    print(customer_service.name)
    print(accounting.name)
    print(HR.name)

    sales.add_employees ("Pam Beesly")
    sales.add_employees("Jim Halpert")
    sales.add_employees("Andy Bernard")
    sales.add_employees("Ryan Howard")
    sales.add_employees("Stanley Hudson")
    sales.add_employees("Phyllis Lapin-Vance")
    print("Sales Employees: ", sales.get_employees())

    print("Customer Service: ", customer_service.get_employees())

    accounting.add_employees("Angela Martin")
    accounting.add_employees("Kevin Malone")
    print("Accounting Employees: ", accounting.get_employees())

    HR.add_employees("Holly Flax")
    print("HR Employees: ", HR.get_employees())

    print("Sales budget: ", sales.budget)
    print("Customer Service budget: ", customer_service.budget)
    print("Accounting budget: ", accounting.budget)
    print("HR budget: ", HR.budget)


    print(accounting.meet())
    print(sales.meet())





