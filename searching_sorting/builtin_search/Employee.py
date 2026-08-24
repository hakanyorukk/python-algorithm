class Employee:
    def __init__(self,name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"{self.name} {self.department} {self.salary}"

    def __repr__(self):
        return f"{self.name} {self.department} {self.salary}"