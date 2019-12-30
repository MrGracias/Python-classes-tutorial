'''
Created on Dec 29, 2019

@author: ogracias
'''
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Oscar'
emp_1.last = 'Gracias'
emp_1.email = 'oscar.gracias@icloud.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@icloud.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)





