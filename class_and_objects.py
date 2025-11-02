class employees:
    language = "python"
    salary = 100000

    def detail(self):
        print(f"the language is {self.language}\n the salary is {self.salary}")

object = employees()

object.detail()
