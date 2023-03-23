from lib.employee import *
from lib.manager import *

# Test your code here

# e.g.
m1 = Manager( 'Mr. Levi', 'HR', 31 )
m2 = Manager('Boss man', 'IT', 20)
e1 = Employee( 'Norris', 4000, m1 )
e2 = Employee( 'Gail', 3000, m1 )

e3 = Employee( 'Rob', 3000, m2 )


print(Employee.find_by_department('IT').name)

print()
for em in e2.tax_bracket():
    print(em.name)

print()
for em in Employee.paid_over(2000):
    print(em.name)

print()
print(Manager.average_age())

print()
m2.hire_employee('Gailly', 5000)

for employee in m2.employees:
    print(employee.name, employee.salary)







# do not remove
#import ipdb; ipdb.set_trace()
