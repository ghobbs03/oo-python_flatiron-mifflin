import statistics

class Manager:
    all = []
    def __init__(self, name, department, age):
        self.name = name
        self.age = age
        self.department = department
        self.employees = []
        Manager.all.append(self)


    def hire_employee(self, name, salary):
        from .employee import Employee
        employee = Employee(name, salary, self)


    def add_employee(self, employee):
        self.employees.append(employee)

    @classmethod
    def all_departments(cls):
        return [manager.department for manager in Manager.all]
    
    @classmethod
    def average_age(cls):
        return statistics.fmean([manager.age for manager in Manager.all])
    