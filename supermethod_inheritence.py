class Manager:
    def __init__(self):
        print("Constructor of Manager")
        self.a = 1


class Employee(Manager):
    def __init__(self):
        super().__init__()     # call Manager
        print("Constructor of Employee")
        self.b = 2


class Worker(Employee):
    def __init__(self):
        super().__init__()     # call Employee
        print("Constructor of Worker")
        self.c = 3


w = Worker()





        
