class Employee:
    all = []
    def __init__(self, name, salary, manager):
        self.name = name
        self.salary = salary
        self.manager = manager
        manager.add_employee(self)
        Employee.all.append(self)
    

    def manager_name(self):
        return self.manager.name

    @classmethod
    def paid_over(cls, starting_salary):
        return [employee for employee in cls.all if employee.salary > starting_salary]
    
    @classmethod
    def find_by_department(cls, department_name):
        from .manager import Manager
        for employee in cls.all:
            print(employee.manager.department)
            if (employee.manager.department == department_name):
                return employee

        return None
    

    def tax_bracket(self):
        return [employee for employee in Employee.all if (employee.salary - 1000 <= (self.salary) <= employee.salary + 1000) and employee != self ]