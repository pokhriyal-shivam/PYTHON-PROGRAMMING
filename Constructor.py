class employees:
    language = "python"
    salary = 100000

# constructor always called automatically  when we create object
    def __init__(self):
        print("this is the constructor")

    def detail(self):
        print(f"the language is {self.language}\n the salary is {self.salary}")

object = employees()

object.detail()
